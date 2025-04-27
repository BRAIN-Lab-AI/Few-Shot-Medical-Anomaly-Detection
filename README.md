# PG-Attention: Prompt-Guided Attention Adapter for Multi-View Few-Shot Medical Anomaly Detection


## Introduction
MVFA-AD Enhanced builds on the original [MVFA-AD repository](https://github.com/MediaBrain-SJTU/MVFA-AD) repository by incorporating intelligent text prompting and an advanced adapter design using attention mechanisms. The improved architecture boosts few-shot anomaly detection performance across diverse medical image modalities such as brain MRI, liver CT, and retinal OCT.

Our enhancements center on:

Prompt Engineering: Designing task-specific, domain-aware prompts that better align with visual cues.

Attention-Enhanced Adapters: Integrating AdapterWithAttention modules that leverage self-attention to improve representation adaptation.

## Project Metadata
### Authors
- **Team:** Alhanoof Alhunief 
- **Supervisor Name:** Dr. Muzammil Behzad
- **Affiliations:** KFUPM

### Project Documents
- **Presentation:** [Project Presentation](/Presentation.pptx)
- **Report:** [Project Report](/PG-Attention.pdf)

### Reference Paper
- [Adapting Visual-Language Models for Generalizable Anomaly Detection in Medical Images](https://openaccess.thecvf.com/content/CVPR2024/papers/Huang_Adapting_Visual-Language_Models_for_Generalizable_Anomaly_Detection_in_Medical_Images_CVPR_2024_paper.pdf)


## Project Technicalities

### Terminologies
- **CLIP Model:** Vision-language model used for text-to-image feature alignment.
- **Adapter Module:** Lightweight fine-tunable module inserted in large pre-trained models.
- **Few-Shot Learning:** Training with only a small number of samples per class.
- **Prompt Engineering:** Designing natural language text prompts to guide CLIP feature extraction.
- **Self-Attention:** Mechanism for learning dependencies between features.

### Problem Statements
- **Problem 1:** Generic prompts in zero/few-shot tasks lead to sub-optimal alignment with medical image features.
- **Problem 2:** Plain MLP adapters may not capture critical inter-token relationships in the image embeddings.


### Proposed Enhancements

#### 1. Prompt Engineering
A new set of medically-informed prompts was developed to improve vision-language alignment. Examples include:
```python
TEMPLATES = [
    "a medical image of a normal {}.",
    "a scan showing disease in the {}.",
    "an image of an abnormal {} under a microscope.",
    # ... (13 total templates)
]
REAL_NAME = {
    'Brain': 'brain',
    'Liver': 'liver',
    'Retina_RESC': 'retina (OCT)',
    'Chest': 'chest X-ray',
    'Retina_OCT2017': 'retina (OCT)',
    'Histopathology': 'histopathological tissue'
} 
```

#### 2. Attention-Enhanced Adapters

The AdapterWithAttention replaces the standard MLP-only adapters with:
- Self-attention blocks
- Layer normalization
- Residual MLPs


## Model Workflow

1. **Few-Shot Training Pipeline**
   ``` python
   python train_few.py --obj Liver --shot 4
   ```
  - Performs anomaly detection using CLIP + AdapterWithAttention
  - Uses advanced prompt templates
  - Stores model checkpoints in ./ckpt/few-shot/

2. **Dataset Support**
   - Liver: https://drive.google.com/file/d/1xriF0uiwrgoPh01N6GlzE5zPi_OIJG1I/view?usp=sharing
   - Brain: https://drive.google.com/file/d/1YxcjcQqsPdkDO0rqIVHR5IJbqS9EIyoK/view?usp=sharing
   - HIS: https://drive.google.com/file/d/1hueVJZCFIZFHBLHFlv1OhqF8SFjUVHk6/view?usp=sharing
   - RESC: https://drive.google.com/file/d/1BqDbK-7OP5fUha5zvS2XIQl-_t8jhTpX/view?usp=sharing
   - OCT17: https://drive.google.com/file/d/1GqT0V3_3ivXPAuTn4WbMM6B9i0JQcSnM/view?usp=sharing

## How to Run the Code

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/yourusername/MVFA-AD-enhanced.git
    cd MVFA-AD-enhanced
    ```

2. **Set Up the Environment:**
    Create a virtual environment and install the required dependencies.
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate
    pip install -r requirements.txt
    ```
    
3. **Quick Start**
   ``` bash
   python test_few.py --obj $target-object --shot $few-shot-number
   ``` 
   For example, to test on the Brain MRI with k=4, simply run:
   ``` bash
   python test_few.py --obj Brain --shot 4
   ```
   
4. **Train the Model:**
   ``` bash
   python train_few.py --obj $target-object --shot $few-shot-number
   ```
   For example, to train on the Brain MRI with k=4, simply run:
   ``` bash
   python train_few.py --obj Brain --shot 4
   ```


## Acknowledgments
MediaBrain-SJTU for the original MVFA-AD repo.



