## Pali Dictionary Project
### Introduction
Loading..

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
    <br>
4. `suttas.csv`
    <br>

### To-do-list
1. Word Matching
    <br>Identify sentences containing the target Pali word, recognizing its various forms (e.g., declensions - nouns and conjugations - verbs). 
    - Extract meaningful & relavant data as much as possible from `vocab_class_*.csv`.
2. Relevance Filtering
    <br>

### Rule-based Approach
Loading..

### AI-based Approach
To process multiple requests asynchronously in the background. Instead of sending each request individually, upload them in a `JSONL` file and `OpenAI` processes them asynchronously.

#### Workflow
1. User submits a question → Save it with a unique identifier in `requests.jsonl`.
2. Every 1 minute → Submit a batch job.
3. Monitor the batch → Download results when completed.
4. Send responses to users

### Relevant Discussion
1. https://github.com/digitalpalidictionary/dpd-db/discussions/33
2. https://github.com/digitalpalidictionary/dpd-db/issues/45