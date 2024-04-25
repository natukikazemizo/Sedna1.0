#!BPY
# -*- coding: UTF-8 -*-
# Think
# 思考
# 2027.09.10 N-mizo(Natukikazemizo)

import calculation
import comparison
import emotion
import filter_input
import filter_output
import imagination
import input
import judgment
import output
import prediction
import unconscious_intervention

class Think:
    def __init__(self, concentration, delta):
        self.concentration = concentration

    def think(self, trigger):
        """Think and output memories and actions.
           思考して、記憶と行動を出力する。

        Parameters
        ----------
        trigger: Any
            Thought trigger/思考の切っ掛け
        """

        # init units
        # 思考単位の初期化
        input_unit = input.Input()
        unconscious_intervention_unit = \
            unconscious_intervention.UnconsciousIntervention()
        filter_input_unit = filter_input.FilterInput()
        emotion_unit = emotion.Emotion()
        imagination_unit = imagination.Imagination()
        comparison_unit = comparison.Comparison()
        calculation_unit = calculation.Calculation()
        prediction_unit = prediction.Prediction()
        judgment_unit= judgment.Judgment()
        filter_output_unit = filter_output.FilterOutput()
        output_unit = output.Output()

        # input cannot be stopped.
        # 思考への情報流入は止められない。
        temporary_memory = input_unit.input(trigger)

        while self.concentration > 0:
            # Uncnsciousness is not tiring.
            # 無意識は疲れを知らない。
            if unconscious_intervention_unit.intervention(temporary_memory):
                break

            # Thinking consumes concentration.
            # 思考すると集中力が下がっていく。
            self.concentration -= self.delta

            temporary_memory = filter_input_unit.filter(temporary_memory)
            temporary_memory = emotion_unit.emote(temporary_memory)
            temporary_memory = imagination_unit.imagine(temporary_memory)
            temporary_memory = comparison_unit.compare(temporary_memory)
            temporary_memory = calculation_unit.calculate(temporary_memory)
            temporary_memory = prediction_unit.prediction(temporary_memory)

        action, temporary_memory = judgment_unit.judge(temporary_memory)
        # Output filter is last resort.
        # 出力フィルターは最後の砦。
        action, temporary_memory = filter_output_unit.filter(action, temporary_memory)
        
        # Remember thoughts and put them into action.
        # 思考結果を記憶し、行動に移す。
        output_unit.output(action, temporary_memory)


    def __del__(self):
        # freedom from thinking
        # 思考からの解放
        self.concentration = 0
