
<h1 align="center">
    STaRK: Benchmarking LLM Retrieval on Textual and Relational Knowledge Bases
</h1>


<div align="center">

[![](https://img.shields.io/badge/paper-pink?style=plastic&logo=GitBook)](https://arxiv.org/abs/2404.13207)
[![](https://img.shields.io/badge/-github-green?style=plastic&logo=github)](https://github.com/snap-stanford/stark) 
</div>

## What is STaRK?
STaRK is a large-scale semi-structure retrieval benchmark on Textual and Relational Knowledge Bases. Given a user query, the task is to extract nodes from the knowledge base that are relevant to the query. 


<figure class="center-figure">
    <img src="media/overview.png" height="350">
</figure>



## Why STaRK?
- **Novel Task**: Recently, large language models have demonstrated significant potential on information retrieval tasks. Nevertheless, it remains an open
question how effectively LLMs can handle the complex interplay between textual and relational
requirements in queries.

- **Large-scale and Diverse KBs**: We provide three large-scale knowledge bases across three areas, which are constructed from public sources.

    <figure class="center-figure"> <img src="media/kb.jpg" height="550"></figure> 

- **Natural-sounding and Practical Queries**: The queries in our benchmark are crafted to incorporate rich relational information and complex textual properties, and closely mirror questions in real-life scenarios, e.g., with flexible query formats and possibly with extra contexts.

    <figure class="center-figure"> <img src="media/questions.jpg" height="350"></figure> 


# Access benchmark data

## 1) Env Setup
Please install the required packages in `requirements.txt`.

## 2) Data download and loading 

[under construction, will be made available very soon!]

## Reference 

```
@article{wu24stark,
    title        = {STaRK: Benchmarking LLM Retrieval on Textual and Relational Knowledge Bases},
    author       = {
        Shirley Wu and Shiyu Zhao and 
        Michihiro Yasunaga and Kexin Huang and 
        Kaidi Cao and Qian Huang and 
        Vassilis N. Ioannidis and Karthik Subbian and 
        James Zou and Jure Leskovec
    },
    eprinttype   = {arXiv},
    eprint       = {2404.13207},
  year           = {2024}
}
```
