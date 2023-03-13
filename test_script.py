from DeepWhiskerCuts.lib.ProgressManager import ExperimentManager
from DeepWhiskerCuts.lib.pipeline import analyze_videos
from DeepWhiskerCuts.setting.dlc_setting import eye_shuffle
import os
import pdb
dir = r'C:\sidevideos\ar37motor\2023_02_22'
manager = ExperimentManager(dir,'side')
for triali in manager.trials:
    if not triali.finished:
        manager.fix_trial(triali)
print('done')