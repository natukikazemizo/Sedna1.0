# bones_custom_object_set_linked
ボーンのカスタムオブジェクトをリンクされたオブジェクトに修正する。
## 開発者
Nミゾ(Natukikazemizo)
## 原因
　カスタムオブジェクトCtrlPic.blendファイルを Linkした際に、CtrlPicコレクションとは別に、CtrlPic.001コレクションが出来てしまった。
CtrlPic.001コレクション無いのオブジェクトは、CtrlPic.blendとのリンクが切れている。
## 問題点
1. CtrlPic.001コレクション内のオブジェクトをArmatureのboneに指定していた場合、他の.blendファイルにLINKしてLinkOverrideした際にCtrlPicが増殖してしまう。
2. ArmatureのboneにCustom Objectを設定するさいに、選択肢が二つ出てきて面倒
3. CtrlPic.001コレクション内のオブジェクトを単純に削除してしまうと、Custom Objectが消えたボーンが大量に発生する。

## 実装案
* 全Objectでループ
  * Armatureだったら
    * 全boneでループ
      * bone.custom_object.libraryが無かったら
         * bone.objectに  
         bpy.data.collections["CtrlPic"].objects["custom_object.name"]
         を設定






