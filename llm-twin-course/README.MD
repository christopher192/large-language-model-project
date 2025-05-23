## LLM Twin Course (End-To-End Framework For Production-Ready LLM System)
### Introduction
As a software developer with hands-on experience in machine learning, I have worked on model development but have had limited exposure to building complete, end-to-end system. This course will help me to expand my understanding of how to design and implement an end-to-end pipeline for production-ready large language model (LLM) system. The LLM Twin Course (End-To-End Framework for Production-Ready LLM System) provides a comprehensive and practical roadmap to achieving this goal.

### Architecture of The LLM Twin
1. Data Collection Pipeline
    - Crawl digital data from various social media platforms, such as `Medium`, `Substack` and `GitHub`.
    - Clean, normalize and load the data to a `Mongo DB` through a series of `ETL` pipelines.
    - Send database changes to a `RabbitMQ` queue using the `CDC pattern`.
    - Package the crawlers as `AWS Lambda` functions.
2. The Feature Pipeline
    - Consume messages in real-time from a queue through a `Bytewax` streaming pipeline.
    - Every message will be cleaned, chunked, embedded and loaded into a `Qdrant` vector DB.
3. The Training Pipeline
4. The Inference Pipeline

### Reference/ Useful Resource
1. https://www.comet.com/site/blog/an-end-to-end-framework-for-production-ready-llm-systems-by-building-your-llm-twin/
2. https://github.com/decodingml/llm-twin-course
3. https://github.com/PacktPublishing/LLM-Engineers-Handbook
4. https://github.com/SylphAI-Inc/LLM-engineer-handbook
5. https://decodingml.substack.com/p/an-end-to-end-framework-for-production


Part 1: https://medium.com/decodingml/an-end-to-end-framework-for-production-ready-llm-systems-by-building-your-llm-twin-2cc6bb01141f
<br>Part 2: https://medium.com/decodingml/your-content-is-gold-i-turned-3-years-of-blog-posts-into-an-llm-training-d19c265bdd6e
<br>Part 3: https://medium.com/decodingml/i-replaced-1000-lines-of-polling-code-with-50-lines-of-cdc-magic-4d31abd3bc3b
<br>Part 4: https://medium.com/decodingml/sota-python-streaming-pipelines-for-fine-tuning-llms-and-rag-in-real-time-82eb07795b87
<br>Part 5: https://medium.com/decodingml/the-4-advanced-rag-algorithms-you-must-know-to-implement-5d0c7f1199d2
<br>Part 6: https://medium.com/decodingml/turning-raw-data-into-fine-tuning-datasets-dc83657d1280