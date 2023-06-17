convert_location_4_IK_FK.py  
===
IK/FK切替用の、コントロールボーンの位置変更処理  

# 開発目的
キャラクター：DDEの両手両脚のIK/FKを切り替えた際に、コントロールボーンの親子関係が切り替わるため、コントロールボーンが勝手に動いてしまう。手作業でもコントロールボーンの位置を修正できるが、作業に三十分～一時間程度かかってしまうため、本処理を開発する。
# 処理概要
あるフレームにおける、ボーンの世界座標(World Location)を取得し、オフセットフレーム後のフレームのボーンに世界座標をボーンのローカル座標に変換して書き込む。

# 技術的補足
## ボーンの座標変換
### 目的
ローカル座標 $\vec{P}$ 世界座標: $\vec{X}$ であるボーン $A$ を世界座標 $\vec{Y}$ に移動する。この世界座標 $\vec{Y}$ に移動した後ののボーン $A$ のローカル座標 $\vec{Q}$ を求めたい。なお、ボーン $A$ の原点の世界座標を $\vec{O}$ とする。  
ボーン $A$ のローカル座標 $\vec{P}$ は、ボーン $\vec{A}$ の世界座標 $\vec{X}$ とボーン $A$ の原点 $\vec{O}$ の差なので、  
$\vec{P}=\vec{X}-\vec{O}$  
となり、式を変形すると  
$\vec{O}=\vec{X}-\vec{P}$  (式1)  
となります。

一方求めたいローカル座標 $\vec{Q}$ は、ボーン $A$ の移動後の世界座標 $\vec{Y}$ とボーン $A$ の原点 $\vec{O}$ の差なので  
$\vec{Q}=\vec{Y}-\vec{O}$  
となります。そこで、(式1)を代入すると、  
$\vec{Q}=\vec{Y}-(\vec{X}-\vec{P}）$  (式2)  
となります。

# 処理説明
## Enum
* 座標の取得元：CoordinateSrc
  * Bone, Origin
* ボーンの部位：PartOfBone
  * Head, Tail, Location
* 四肢：Limb
  * Arm_L, Arm_R, Leg_L, Leg_R)


## 定数
* 処理対象Armature名：ARMATURE_NAME
* 変換元のFrame：ORG_FRAME
* 変換後のFrameとの差：OFFSET_FRAME
* IK/FK切替用のボーン名：IK_FK_CHG_BONE
  * 左腕用：PIN_ARM_L
  * 右腕用：PIN_ARM_R
  * 左脚用：PIN_LEG_L
  * 右脚用：PIN_LEG_R
* FKモードに切り替えられたと判定する最小値：MIN_FK
* 座標変換対象のボーン名：trans_bone_names
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
    {Arm_L:PIN_ARM_L},{Arm_R:PIN_ARM_R},{Leg_L:PIN_Leg_L},{Leg_R:PIN_Leg_R}
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
  * trans_bone_namesでループ
    * trans_bone_names[i]でボーン変換辞書よりボーン変換を取得
    * IK/FK判定
      * ボーン変換.四肢 と、IK/FK切替ボーン辞書より、IK/FK切替判定用のボーン名を取得する。
      * IK/FK切替判定用のボーン名のLocal座標の長さ＞MIN_FK　の場合、FKと判定する。
      そうでない場合は、IKと判定する。
    * 移動先座標取得
      * 座標記録用の辞書よりボーン座標を取得する。IKの場合はIK用座標を、FKの場合はFK用座標を取得する。
    * 変換後座標設定
      * trans_bone_names[i]のボーンの


* 終了処理
  * Current FrameをORG_FRAMEにする



元Frame
Frameのオフセット値
Current Frameに元フレームを設定
ボーンペアリストでループ
IK/FKで位置が変1わるボーンの元フレームのWorld Location：org_w_locationを取得し、保持しておく
変換先フレーム（変更元フレーム＋オフセットフレーム数で計算）にカレンとフレームを切り替える
ボーンのLocal Location:new_l_locaton と World Location：new_w_location を取得する
ボーンのLocal Location に
org_w_location - (new_w_location - new_l_location)
を設定する。

# 制限事項


