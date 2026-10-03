operation Main() : Result {
    use q = Qubit();
    H(q);               // 重ね合わせを作成
    return MResetZ(q);  // 測定してリセット
}