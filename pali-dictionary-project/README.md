## Pali Dictionary Project
### Introduction
This project involves volunteer work to support part of development of the `digitalPālidictionary/dpd-db`, a resource for the `Sāsanārakkha Buddhist Sanctuary` Monk Training Centre. The goal is to enhance Pali language studies, sutta analysis, and Dhamma teachings through structured datasets & documents, processing techniques and AI solution.

### Problem Statement
Extracting Pali sentences based on a given Pali word from exercise data cannot rely solely on regular expressions due to the unstructured nature of the text. Pali’s rich inflectional morphology, such as declensions and conjugations, create variations that simple regex patterns cannot effectively handle. Additionally, special markers like `simpl`, `$`, and `%` require careful handling, and ensuring accurate source referencing adds further complexity. The extracted sentence must also include its English translation, with the source reference clearly provided.

### Dataset Description
1. `vocab_class_*.csv`
    - <b>id</b> - Unique identifier for each Pali word entry.
    - <b>pali</b> - The Pali word, including declensions and conjugations.
    - <b>pos</b> - Part of Speech, the grammatical category of the word (e.g., noun, verb, adjective).
    - <b>meaning</b> - The English meaning of the Pali word.
    - <b>source_1</b> - The first source where the word appears (e.g., Sutta number).
    - <b>sutta_1</b> - The name of the sutta where the word appears
    - <b>example_1</b> - An example sentence from the sutta using the word in context.
    - <b>source_2</b> to <b>source_4</b> - Additional sources where the word appears, following the same structure as <b>source_1</b>.

2. `exercises_class_*.txt`
    <br>This dataset contains `Pali sentences` with their corresponding `English translations` and references from various `Buddhist scriptures`. The dataset is useful for `Pali language studies`, `sutta analysis`, and `Dhamma teachings`. 
    <br><br>Important document data for extraction
    - <b>Canonical Source</b> - MN, SN, DN, DHP, VIN, AN, UD, SNP, TH..
    - <b>Sutta Number</b> - 22.33, 3.21, 16.32..
    - <b>Pali Sentence</b>
    - <b>English Meaning of The Pali Sentence</b>
3. `output_class_*.txt`
    <br>These files store the LLM batch processing `results` for Pali sentence extraction. The data will help to assess the accuracy of LLM.
4. `suttas.csv`
    <br>This `CSV` file maps sutta numbers to their corresponding sutta names.
5. `new_suttas.csv`
    <br>A refined version of `suttas.csv` with improved formatting for better readability and usability.

### Project Expectation
1. Identify sentence containing the target Pali word, recognizing its various forms (e.g., declensions - nouns and conjugations - verbs). 
    - Extract meaningful & relavant data as much as possible from `vocab_class_*.csv` as input to LLM.
2. For each Pali word, extract a single relevant sentence and its english translation from the exercise data.
3. Include the source reference for the extracted sentence.
    -  If it is marked as `simpl`, preserve it.
4. Pick the sentence in the exercise data that has source reference and is not marked by `$` or `%`.
5. If the source reference of the extracted sentence does not match any of it from `vocab_class_2.csv`, the system should flag this case for manual review. (Ignore first until further instruction)

### Rule-based Approach
(Details to be added)

### AI-based Approach
To process multiple requests asynchronously in the background. Instead of sending each request individually, upload them in a `JSONL` file and `OpenAI` processes them asynchronously.

#### Workflow 1
1. User submits a question → Save it with a unique identifier in `requests.jsonl`.
2. Every 1 minute → Submit a batch job.
3. Monitor the batch → Download results when completed.
4. Send responses to users

#### Workflow 2
1. User inputs a `Pali` word.
2. Search for the matching `Pali` word in the `pali_class/vocab/*` directory.
3. If a match is found:
    - Retrieve its ID, meaning, part of speech (POS) and relevant declensions/ conjugations.
    - Get the `exercise number` based on vocab_class_*.csv, for example vocab_class_2.csv then find the exercises_class_2.txt.
    - Identify the exercise number based on the matching `vocab_class_*.csv` file (e.g., `vocab_class_2.csv` > `exercises_class_2.txt`).
    - Locate the corresponding exercise file `exercises_class_*.txt` for document check.
4. Design `SYSTEM_PROMPT` & `USER_PROMPT`.

### To-do List (Start from 1 April 2025)
| No | Task | Description | Complete Date | Status |
| --- | -------- | --- | --- | --- |
| 1 | Manually Retrieve Sutta Names by Sutta Number | - | N/A | &cross; |
| 2 | Generate Ground Truth Data | - | N/A | &cross; |
| 3 | Compare Restructured Exercise vs. Original Exercise | - | N/A | &cross; |
| 4 | Experiment with JSON Output Behavior of LLM Model | - | N/A | &cross; |
| 5 | Optimize LLM Prompt | - | N/A | &cross; |
| 6 | Conduct More Experiment with Meaningful Input Data | - | N/A | &cross; |
| 7 | Multi-LLM Framework | LangChain, LlamaIndex, LightRAG, Autogen, etc | N/A | In Progress |
| 8 | DeekSeek Experiment | Evaluate the efficiency of an LLM in extracting Pali sentence | N/A | In Progress |
| 9 | Gemini Experiment | Evaluate the efficiency of an LLM in extracting Pali sentence | N/A | In Progress |
| 10 | Vector Database | Milvus, Weaviate, etc For Storing Pali Exercise Data | N/A | &cross; |
| 11 | Agent Framework | MANUS AI for Agent to Optimize LLM Prompts, Preprocessing Agent, Postprocessing Agent | N/A | &cross; |
| 12 | Prompt Management Framework | - | N/A | &cross; |
| 13 | DevOps Backend | - | N/A | &cross; |
| 14 | LLMOps | - | N/A | &cross; |
| 15 | Open Source LLM | Ollama, Hugging Face, etc | N/A | &cross; |
| 16 | Cloud | AWS, Azure, etc | N/A | &cross; |

### Existing Issue
1. Sometimes, the `JSON` response does not match expectations. To resolve this, the system should explain why it generated a particular response when asked.
    - Example: User question: Why is "class_example": "sāvako `<b>`dhammaṃ anussarati`</b>`" returned instead of "class_example": "sāvako dhammaṃ `<b>`anussarati`</b>`"? How can I ensure it returns "class_example": "sāvako dhammaṃ `<b>`anussarati`</b>`"? in `USER_PROMPT`.
2. Invalid `JSON` output, eg output as ```json { ... } ``` instead of `{ ... }`. 
    - Programmatically fix this by remove markdown code block.
    - 2 API calls, if `JSON` parsing still fails after first API, ask the API again for a valid `JSON` format.
    - If the output format is consistently ```json { ... }```, do not prompt the model to return ```{ ... }```. Instead, handle the formatting programmatically.
    - Utilize function calling - https://platform.openai.com/docs/guides/function-calling
    - Utilize structured output - https://platform.openai.com/docs/guides/structured-outputs
3. LLM struggles to map a `sutta number` to its corresponding `sutta name`.
    - Simple rule-based lookup system instead of relying on an LLM. Example, extract sutta name based on sutta number from `new_suttas.csv`.
    - If the LLM is not confident about the mapping, refers to the `CSV` instead of guessing.
4. Instead of focusing on crafting the perfect prompt, would improving (more structured) the `exercise data` and `input` help the LLM perform better?
    - Check `restructured_exercises_class_*.txt`.
5. Unicode character issue
    - `UnicodeDecodeError` when saved the data to .csv, need to evaluate further. 

### Relevant Discussion
1. https://github.com/digitalpalidictionary/dpd-db/discussions/33
2. https://github.com/digitalpalidictionary/dpd-db/issues/45
3. https://github.com/sasanarakkha/dpd-db-sbs/issues/1
4. https://github.com/sasanarakkha/dpd-db-sbs/issues/25

### Reference
<b>POS (part of speech) Categories</b>
- masc (Masculine, likely for nouns)
- fem (Feminine, likely for nouns)
- nt (Neuter, likely for nouns)
- pr (Pronoun or Proper noun)
- imp (Imperative, verb mood)
- pp (Past participle)
- ind (Indicative, verb mood)
- adj (Adjective)

<b>Prompt Technique:</b> https://www.kaggle.com/whitepaper-prompt-engineering