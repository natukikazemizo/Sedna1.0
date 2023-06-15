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
ローカル座標：$\vec{P}$ 世界座標：$\vec{X}$ であるボーン$A$ を世界座標$\vec{Y}$ に移動する。この世界座標$\vec{Y}$ に移動した後ののボーン$A$ のローカル座標$\vec{Q}$ を求めたい。なお、ボーン$A$ の原点の世界座標を$\vec{O}$ とする。  
ボーン$A$のローカル座標$\vec{P}$は、ボーン$\vec{A}$ の世界座標$\vec{X}$ とボーン$A$ の原点$\vec{O}$ の差なので、  
$\vec{P}=\vec{X}-\vec{O}$  
となり、式を変形すると  
$\vec{O}=\vec{X}-\vec{P}$  (式1)  
となります。

一方求めたいローカル座標$\vec{Q}$は、ボーン$A$ の移動後の世界座標$\vec{Y}$ とボーン$A$ の原点$\vec{O}$ の差なので  
$\vec{Q}=\vec{Y}-\vec{O}$  
となります。そこで、(式1)を代入すると、  
$\vec{Q}=\vec{Y}-(\vec{X}-\vec{P}）$  (式2)  
となります。

# 処理説明
## Enum
* 位置タイプ：LocationType
  * Head, Tail, Location
* 四肢：Limb
  * Arm_L, Arm_R, Leg_L, Leg_R)

## 定数
* 処理対象Armature名：ARMATURE_NAME
* 変換元のFrame：ORG_FRAME
* 変換後のFrameとの差：OFFSET_FRAME
* IK/FK切替用のボーン名
  * 左腕用：PIN_ARM_L
  * 左腕用：PIN_ARM_R
  * 左腕用：PIN_LEG_L
  * 左腕用：PIN_LEG_R
## 変数
* 
ボーン変換ペアリスト
四肢Enum, IK用のボーン名／位置Enum,FK用のボーン名／位置Enum
IK/FK切替ボーンリスト
右腕／左腕／右足／左足のIK/FK切り替えのボーン名
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


