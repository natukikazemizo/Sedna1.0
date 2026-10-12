$folderPath = "D:\Blender\sounds\BGM"   # ←ここを自分のフォルダに変更

$shell  = New-Object -ComObject Shell.Application
$folder = $shell.Namespace($folderPath)

# よく使うプロパティのインデックス（Windows 10/11でほぼ共通）
$props = @{
    21 = "Title"          # タイトル
    13 = "Artist"         # アーティスト
    14 = "Album"          # アルバム
    27 = "Duration"       # 長さ
    28 = "Bitrate"        # ビットレート
}

$results = foreach ($item in $folder.Items()) {
    if ($item.Name -match '\.(mp3|wav|flac|m4a|ogg)$') {
        $obj = [ordered]@{
            FileName = $item.Name
            FullPath = $item.Path
        }
        foreach ($index in $props.Keys) {
            $obj[$props[$index]] = $folder.GetDetailsOf($item, $index)
        }
        [PSCustomObject]$obj
    }
}

# 結果を表示
$results | Format-Table -AutoSize

# CSVに出力（整理用に便利）
$results | Export-Csv -Path "$folderPath\BGM_Metadata.csv" -Encoding UTF8 -NoTypeInformation
