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
  * ボーン：Bone
  * 原点：Origin
* ボーンの部位：PartOfBone
  * 原点を指定:Zero
  * headの世界座標:Head
  * tailの世界座標:Tail
  * ローカル座標:Location
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
* 設定ファイルのフルパス：SETTING_FILE_PATH
* FKモードに切り替えられたと判定する最小値：MIN_FK  
* 原点(mathutils.Vector(0,0,0)：ORIGIN
## クラス
* 座標の元情報：SrcInfo
  * 変数
    * 座標の取得元：src:BoneOrigin
    * ボーン名：name
    * 部位：part:PartOfBone
    * 世界座標：world_location
  * 関数
    * get_part_location  
     部位に応じた座標を取得
    * set_world_location  
      世界座標設定
    * get_world_location  
     世界座標取得
* ボーン座標変換：BoneTrans
  * 変数
    * ボーン名
    * 四肢
    * 座標の元情報_IK
    * 座標の元情報_FK
  * 関数
    * set_org_location  
      元座標設定  
      IK用とFK用の情報を設定する
    * get_trans_location  
      変換後座標取得  
      * IK/FKの切替判定  
        元フレームと先フレームで、四肢がIK/FKがどう切り替わったか
        判定する。
        IK→FKかFK→IKの場合は座標変換する
        IK→IKかFK→FKの場合は座標変換しない。
      * 座標の取得
        * 座標変換対象のボーンを$B$とする
        * 座標の取得元が「原点」の場合、原点を返却する
        * 座標の取得元が「ボーン」の場合  
          * $B$が、"Hand.L/R"か"Toe.L/R"の場合、IKが有効なままだと座標がズレるので、IKを一時的に無効にする。  
          * $B$のx軸とy軸とz軸から、座標変換用の行列$A$を作成する。
          * $Bの世界座標-(Bのローカル座標\times A)$
          で$B$の原点を求める
          * $(変換先の世界座標 - Bの原点) \times {}^t A $ を計算し、返却する

## 関数
* check_IK_FK:IK/FK判定
  * ボーンのローカルy座標 ＞ MIN_FKの場合、FKと判定
  * 上記以外の場合、IKと判定

* replace_keyframe:F-Curveのキーフレームの置換
  * Armatureとボーン名を頼りにlocationのF-Cureveを探し、フレーム指定でキーフレームの値を引数の値で置換する。

## 処理の流れ
* 変数初期化
  * 四肢に対するIK/FK切替ボーン辞書作成  
    ```
    {Limb.Arm_L:ARM_PIN_L, <<以下略>>}
    ```
  * 設定ファイルからヘッダと本体のデータ取得  
    設定ファイルの内容は、
    [convert_location_4_IK_FK パターン](https://docs.google.com/spreadsheets/d/1_WTIvTkg_w0k1wFJPyg4sHBb2bkfpKs7Nq4aCRMfrUs/edit?usp=sharing)参照
  * ヘッダ行データから、列名辞書の作成
  * 列名辞書と本体行データから、ボーン座標変換辞書を作成する。  
    ボーン座標変換辞書は
    Key:変換対象のボーン名
    Value:ボーン座標変換クラスのインスタンス

* 元フレームの座標記録
  * Current FrameをORG_FRAMEにする
  * ボーン座標変換辞書のKeyでループ
    * keyで、ボーン座標変換クラスのインスタンス取得
    * ボーン座標変換クラスのインスタンス.元座標設定 で、IK用とFK用の情報を設定

  * 元フレームの四肢のIK/FKの辞書を作成する。

* 変換後の座標の反映
  * Current FrameをORG_FRAME + OFFSETにする
  * 先フレームの四肢のIK/FKの辞書を作成する。
  * ボーン座標変換辞書のKeyでループ
    * keyで、ボーン座標変換クラスのインスタンス取得
    * ボーン座標変換クラスのインスタンス.変換後座標取得　で変換後座標を取得し、F-Cureveに反映する。

* 終了処理
  * Current FrameをORG_FRAMEにする  

# 制限事項
* FKモードの際、手足が自由に伸びるようになっています。ですので、FKモードからIKモードに座標を変換した時に、手足が勝手に伸縮してしまいます。FKモードからIKモードに変換するさいは、FKモードのフレームであらかじめ手足が通常の長さになるようにポーズ修正しておくと、手足の勝手な伸縮が小さくなります。

