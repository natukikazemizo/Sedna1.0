convert_location_4_IK_FK.py  
===
IK/FK切替用の、コントロールボーンの位置変更処理  
2023.06.04 Natukikazemizo（Nミゾ）新規作成

# 開発目的
キャラクター：DDEの両手両脚のIK/FKを切り替えた際に、コントロールボーンの親子関係が切り替わるため、コントロールボーンが勝手に動いてしまう。手作業でもコントロールボーンの位置を修正できるが、作業に三十分～一時間程度かかってしまうため、本処理を開発する。
# 処理概要
あるフレームにおける、ボーンの世界座標(World Location)を取得し、オフセットフレーム後のフレームのボーンに世界座標をボーンのローカル座標に変換して書き込む。

# 技術的補足
## 世界座標とボーン座標の座標変換
### 前提
ボーンの原点の世界座標  $\vec{B_{o}}$  
ボーンのローカル座標   $\vec{L}$  
ボーン座標の単位ベクトル   $\vec{B_{x}}, \vec{B_{y}}, \vec{B_{z}}$  
求めたい世界座標  $\vec{W}$  

$`
A=\begin{pmatrix}
\vec{B_{x}}\\
\vec{B_{y}}\\
\vec{B_{z}}
\end{pmatrix}
`$

### ボーン座標を世界座標に変換  
$\vec{W}=\vec{B_{o}}+\vec{L}\times{A}$  

### 世界座標をボーン座標に変換
$\vec{L}=(\vec{W}-\vec{B_{o}})\times{}^tA$  

## ボーンの座標変換
### 前提
ボーン $B$  
ボーンの原点の世界座標 $\vec{W_{ω}}$   
ボーン座標の単位ベクトル   $\vec{B_{x}}, \vec{B_{y}}, \vec{B_{z}}$  

$'
A=
\begin{pmatrix} 
\vec{B_{x}} \\ 
\vec{B_{y}} \\
\vec{B_{z}}
\end{pmatrix} 
'$



移動前の世界座標  $\vec{W_{α}}$  
移動前のローカル座標  $\vec{B_{p}}$  

移動先の世界座標  $\vec{W_{β}}$  
移動先のローカル座標  $\vec{B_{q}}$

### 目的
 $\vec{W_{α}}$ で $\vec{B_{p}}$ だったボーン $B$ を  $\vec{W_{β}}$ に移動した際のローカル座標  $\vec{B_{q}}$ を求めたい。  
   
ボーン $B$ のローカル座標 $\vec{B_{p}}$ を世界座標に変換すると、ボーン $B$ の世界座標 $\vec{W_{α}}$  と $\vec{W_{ω}}$ の差と等しくなるので

$\vec{B_{p}} \times A=\vec{X}- \vec{W_{ω}} $  
となり、式を変形すると  
$\vec{W_{ω}}=\vec{W_{α}}-(\vec{B_{p}} \times A)$  
となります。

一方求めたいローカル座標 $\vec{B_{q}}$ は、ボーン $B$ の移動後の世界座標 $\vec{W_{β}}$ とボーン $B$ の原点 $\vec{W_{ω}}$ の差を世界座標に変換したものなので、  
$\vec{B_{q}}=(\vec{W_{β}}-\vec{W_{ω}})  \times {}^t A $  
となります。そこで、(式1)を代入すると、  
$\vec{B_{q}}=(\vec{W_{β}}-(\vec{W_{α}}- (\vec{B_{p}} \times A)) \times {}^t A $  
となります。



# 処理説明
## Enum
* 座標の取得元：CoordinateSrc
  * Bone, Origin
* ボーンの部位：PartOfBone
  * Head, Tail, Location
* 四肢：Limb
  * Arm_L, Arm_R, Leg_L, Leg_R
* 運動学：Kinematics
  * IK, FK


## 定数
* 処理対象Armature名：ARMATURE_NAME
* 変換元のFrame：ORG_FRAME
* 変換後のFrameとの差：OFFSET_FRAME
* IK/FK切替用のボーン名
  * 左腕用：ARM_PIN_L
  * 右腕用：ARM_PIN_R
  * 左脚用：LEG_PIN_L
  * 右脚用：LEG_PIN_R
* FKモードに切り替えられたと判定する最小値：MIN_FK  
* ~~座標変換対象のボーン名：trans_bone_names~~
* 原点(Vector型で0,0,0)：ORIGIN
## クラス
* ボーン変換：BoneTransformation
  * 四肢：Limb
  * 座標の取得元_IK：src_IK
  * ボーン名_IK：bone_name_IK
  * ボーンの部位_IK：bone_part_IK
  * 座標の取得元_FK：src_FK
  * ボーン名_FK：bone_name_FK
  * ボーンの部位_FK：bone_part_FK

## 処理の流れ
* 変数初期化
  * IK/FK切替ボーン辞書作成  
    ```
    {Limb.Arm_L:ARM_PIN_L, <<以下略>>}
    ```
  * ボーン変換辞書作成
    * trans_bone_names 全てに対して、ボーン座標クラスのインスタンスを紐づける辞書を作成する。ボーン座標クラスの初期値はベタ書き。
       * 初期値は
[convert_location_4_IK_FK パターン](https://docs.google.com/spreadsheets/d/1_WTIvTkg_w0k1wFJPyg4sHBb2bkfpKs7Nq4aCRMfrUs/edit?usp=sharing)
参照
  * 座標記録用の辞書作成
    * ボーン名が辞書キー　値はIK用とFK用のVector2件

* 元フレームの座標記録
  * Current FrameをORG_FRAMEにする
  * trans_bone_namesでループ
    * trans_bone_names[i]でボーン変換辞書よりボーン変換を取得
    * IK用の座標取得
      * ボーン変換.座標の取得元がBoneの場合
        * ボーン変換.ボーン名_IKを取得
        *  座標記録用の辞書に、ボーンの部位_IKの座標を設定
      * ボーン変換.座標の取得元がOriginの場合
        * 座標記録用の辞書に、ORIGINを設定
    * FK用の座標取得　→　IK用の座標取得と同様に実装するので、関数化？
* 先フレームに変換後座標を設定
  * Current FrameをORG_FRAME+OFFSET_FRAMEにする
  * 四肢のIK/FK判定
    * LimbをKey Kinematicsを値にした四肢運動学辞書を作成
    * Limbでループ
      * IK/FK切替ボーン辞書より、IK/FK切替判定用のボーン名を取得
      * IK/FK切替判定用のボーン名のLocal座標のVectorの長さ＞MIN_FK　の場合、FKと判定する。
      そうでない場合は、IKと判定し、四肢運動学辞書に設定する。
  * trans_bone_namesでループ
    * trans_bone_names[i]でボーン変換辞書よりボーン変換を取得
    * IK/FK判定
      * ボーン変換.四肢 と、四肢運動学辞書よりIK/FKを取得
    * 移動先座標取得
      * 座標記録用の辞書よりボーン座標を取得する。IKの場合はIK用座標を、FKの場合はFK用座標を取得する。
    * 変換後座標設定
      * trans_bone_names[i]で座標設定対象ボーン取得
      * 座標設定対象ボーン.location　に、  
        移動先座標　－　(移動前のボーンの世界座標　－　移動前のボーンのローカル座標)
        を設定

* 終了処理
  * Current FrameをORG_FRAMEにする  

# 制限事項
* 作成中　コーディング時に追記予定

