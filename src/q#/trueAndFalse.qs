import Microsoft.Quantum.Diagnostics.*;
import Microsoft.Quantum.Intrinsic.*;

operation CreateSuperposition() : Unit {
    // 量子ビQ# VSCode 使い方ットを1つ確保（初期状態は False / Zero）
    use q = Qubit();
    
    // アダマールゲートを適用して重ね合わせ状態にする
    H(q);
    
    // （この時点で q は True と False の重ね合わせ）
    Reset(q);
}