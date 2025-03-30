## Pali Dictionary Project
### Introduction
This project involves volunteer work to support part of development of the `digitalPālidictionary/dpd-db`, a resource for the `Sāsanārakkha Buddhist Sanctuary` Monk Training Centre. The goal is to enhance Pali language studies, sutta analysis, and Dhamma teachings through structured datasets & documents, processing techniques and AI solution.

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

### To-do-list
1. Word Matching
    <br>Identify sentences containing the target Pali word, recognizing its various forms (e.g., declensions - nouns and conjugations - verbs). 
    - Extract meaningful & relavant data as much as possible from `vocab_class_*.csv`.
2. Relevance Filtering
    <br>(Details to be added)

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

### Relevant Discussion
1. https://github.com/digitalpalidictionary/dpd-db/discussions/33
2. https://github.com/digitalpalidictionary/dpd-db/issues/45

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

### Existing Issue
1. Sometimes, the `JSON` response does not match expectations. To resolve this, the system should explain why it generated a particular response when asked.
    - Example: User question: Why is "class_example": "sāvako `<b>`dhammaṃ anussarati`</b>`" returned instead of "class_example": "sāvako dhammaṃ `<b>`anussarati`</b>`"? How can I ensure it returns "class_example": "sāvako dhammaṃ `<b>`anussarati`</b>`"? in `USER_PROMPT`.
2. Invalid `JSON` output, eg output as ```json { ... } ``` instead of `{ ... }`. 
    - Programmatically fix this by remove markdown code block. 
    - 2 API calls, if `JSON` parsing still fails after first API, ask the API again for a valid `JSON` format.
    - If the output format is consistently ```json { ... }```, do not prompt the model to return ```{ ... }```. Instead, handle the formatting programmatically.