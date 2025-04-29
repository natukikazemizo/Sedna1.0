<#
Blender用の.pyのランチャー
Blender .py launcher
-------------------------------
2025.04.29 N-mizo
#>
$blender_install_path="C:\Program Files\Blender Foundation\Blender 4.4"
$blend_path="D:\Blender\trunk\Sedna\Animation\CtrlPic.blend"
$py_path="C:\Sync\GitHub\Sedna1.0\src\python\check_output_path.py"
Set-Location $blender_install_path
.\blender.exe -b $blend_path -P $py_path
