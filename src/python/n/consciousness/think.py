#!BPY
# -*- coding: UTF-8 -*-
# Think
#
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

        Parameters
        ----------
        trigger: Any
            Thought trigger.
        """

        # init units
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

        # input cannot be stopped
        temporary_memory = input_unit.input(trigger)

        while self.concentration > 0:
            # Uncnsciousness is not tiring.
            if unconscious_intervention_unit.intervention(temporary_memory):
                break

            # Thinking consumes concentration.
            self.concentration -= self.delta

            temporary_memory = filter_input_unit.filter(temporary_memory)
            temporary_memory = emotion_unit.emote(temporary_memory)
            temporary_memory = imagination_unit.imagine(temporary_memory)
            temporary_memory = comparison_unit.compare(temporary_memory)
            temporary_memory = calculation_unit.calculate(temporary_memory)
            temporary_memory = prediction_unit.prediction(temporary_memory)

        action, temporary_memory = judgment_unit.judge(temporary_memory)
        # Output filter is last resort.
        action, temporary_memory = filter_output_unit.filter(action, temporary_memory)
        
        # Remember thoughts and put them into action.
        output_unit.output(action, temporary_memory)


    def __del__(self):
        # freedom from thinking
        self.concentration = 0
