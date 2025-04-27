TEMPLATES = [
    'a medical image of a normal {}.',
    'a medical image showing an abnormal {}.',
    'a scan showing a healthy {}.',
    'a scan showing disease in the {}.',
    'an image of a normal {} under a microscope.',
    'an image of an abnormal {} under a microscope.',
    'an imaging scan of a healthy {}.',
    'an imaging scan showing anomalies in the {}.',
    'an image of the {} with no abnormalities.',
    'an image of the {} with pathological changes.',
    'an image of a {} used for anomaly detection.',
    'a clean medical scan of the {}.',
    'a medical scan of the {} showing irregularities.',
    
    # More clinical context and terminology
    'a diagnostic scan highlighting a healthy {}.',
    'a diagnostic scan highlighting abnormalities in the {}.',
    'a radiology image showing a normal {}.',
    'a radiology image showing a diseased {}.',
    'a high-resolution scan of the {} without any lesions.',
    'a high-resolution scan of the {} showing abnormal findings.',
    'a medical image capturing early signs of disease in the {}.',
    
    # Contrastive healthy/abnormal pairs
    'a healthy {} compared with an abnormal one in a medical image.',
    'a medical imaging study showing a diseased {}.',
    'a clinical image illustrating typical features of a healthy {}.',
    'a clinical image illustrating atypical features in the {}.',
    'a cross-sectional scan of the {} showing no evidence of pathology.'
]


REAL_NAME = {
    'Brain': 'brain',
    'Liver': 'liver',
    'Retina_RESC': 'retina (OCT)',
    'Chest': 'chest X-ray',
    'Retina_OCT2017': 'retina (OCT)',
    'Histopathology': 'histopathological tissue'
}
