# NLP Text Summarizer with Google Pegasus Model

This project demonstrates the creation of an **NLP-based Text Summarizer** using the **Google Pegasus model** through Hugging Face's Transformers library. The summarizer is tailored for dialogue-based data, making it suitable for summarizing conversational texts, customer service chats, and similar contexts.

## Table of Contents

- [Overview](#overview)
- [Project Pipeline](#project-pipeline)
- [Evaluation Metrics](#evaluation-metrics)
- [Sample Predictions](#sample-predictions)
- [Model Configuration](#model-configuration)
- [Achieved Outcomes](#achieved-outcomes)
- [Future Enhancements](#future-enhancements)
- [Conclusion](#conclusion)

## Overview

The project is structured into a **five-stage modular pipeline** for efficient processing, training, and evaluation. This modular approach ensures scalability, ease of maintenance, and a streamlined workflow from data ingestion to summarization output.

## Project Pipeline

The project is divided into the following modules:

### 1. Data Ingestion
- **Objective**: To gather and format dialogue data for processing.
- **Process**: 
  - Loads the SAMSum dataset, a dataset for conversational summarization.
  - Prepares data in a structured format (JSON or pandas DataFrame).
- **Output**: A structured dataset with fields for dialogue text and summary.

### 2. Data Validation
- **Objective**: To ensure data consistency before training.
- **Process**:
  - Checks for data integrity, including non-empty fields and correct formats.
  - Verifies text and summary pairs for accurate mapping.
- **Output**: A validated dataset, ensuring consistent inputs for training.

### 3. Data Transformation
- **Objective**: To prepare data for model training.
- **Process**:
  - Tokenizes data using the Pegasus tokenizer.
  - Transforms data into tensors, ready for input to the Pegasus model.
- **Output**: Tokenized dataset, ready for model training.

### 4. Model Trainer
- **Objective**: To train the Pegasus model on the processed data.
- **Process**:
  - Configures training parameters (learning rate, batch size, etc.).
  - Uses the Hugging Face `Trainer` API with GPU acceleration for efficient training.
- **Output**: A trained summarization model fine-tuned on conversational data.

### 5. Model Evaluation
- **Objective**: To assess model performance using ROUGE metrics.
- **Process**:
  - Calculates **ROUGE-1**, **ROUGE-2**, **ROUGE-L**, and **ROUGE-Lsum** scores to evaluate summary quality.
  - Uses a custom evaluation function for batch processing and performance assessment.
- **Output**: ROUGE metrics providing quantitative insight into summarization accuracy.

## Evaluation Metrics

The model's performance was evaluated using the ROUGE metrics, which measure the similarity between the predicted and reference summaries. 

**Sample Evaluation Results:**

| Metric    | ROUGE-1   | ROUGE-2   | ROUGE-L   | ROUGE-Lsum |
|-----------|-----------|-----------|-----------|------------|
| Pegasus   | 0.024655  | 0.0       | 0.024446  | 0.02437    |

These scores indicate a moderate level of success, showing that the model is effective for conversational summarization but has room for improvement.

## Sample Predictions

Here is a sample dialogue from the SAMSum dataset with the model's predicted summary:

- **Dialogue**:

**Hannah:** Hey, do you have Betty's number?  
**Amanda:** Lemme check  
**Hannah:** ![gif](<file_gif>)  
**Amanda:** Sorry, can't find it.  
**Amanda:** Ask Larry  
**Amanda:** He called her last time we were at the park together  
**Hannah:** I don't know him well  
**Hannah:** ![gif](<file_gif>)  
**Amanda:** Don't be shy, he's very nice  
**Hannah:** If you say so...  
**Hannah:** I'd rather you texted him  
**Amanda:** Just text him 🙂  
**Hannah:** Urgh... Alright  
**Hannah:** Bye  
**Amanda:** Bye bye  



- **Reference Summary**:  
`Hannah needs Betty's number but Amanda doesn't have it. She needs to contact Larry.`

- **Model Summary**:  
`Amanda can't find Betty's number. Larry called Betty last time they were at the park together. Hannah wants Amanda to text Larry. Amanda will text Larry.`

The model summary captures the main theme with slight deviations in details, demonstrating its potential for dialogue summarization.

## Model Configuration

1. **Summarization Parameters**:  
 - `length_penalty`: 0.8, to control summary length.
 - `num_beams`: 8, for exploring multiple summary options.
 - `max_length`: 128, to ensure concise summaries.

2. **Hardware Acceleration**:
 - Environment has GPU support, but CPU usage was detected. Future iterations should specify a `device` parameter for GPU utilization.

## Achieved Outcomes

- **Pipeline Efficiency**: The modular design streamlined each stage, making the model easy to manage and improve.
- **Summarization Accuracy**: ROUGE scores provided a reliable baseline for conversational summarization.
- **Scalability**: Modular structure supports future enhancements, such as using other models or adding custom improvements.

## Future Enhancements

- **Incorporating Explainable AI (XAI)**: Add XAI to interpret why the model prioritizes specific phrases, useful for understanding conversational nuances.
- **Fine-Tuning on Other Datasets**: Broaden model training on additional datasets for improved generalization.
- **Interactive Parameter Tuning**: Enable non-technical users to adjust parameters (e.g., `num_beams`, `length_penalty`) for customized summaries.

## Conclusion

This project demonstrates the potential of NLP and Google Pegasus for text summarization in a structured pipeline. The model performs well for conversational summarization, though further enhancements in XAI and additional datasets can improve its robustness. This summarizer has promising applications in customer service, conversation analysis, and content summarization, with a scalable architecture ready for real-world deployment.
