# Final-Year-Prpject
AI-Powered Preparation Assistant for
FBISE (Matric FSc) and Entry Tests
(MDCAT ECAT)
Project Team
Ameer Hamza 22i-2579
Saif Ur Rehman 22i-8767
Fizza Sarfraz 22i-0546
Session 2025-2026
Supervised by
Ms. Anum Kaleem
Department of Computer Science
National University of Computer and Emerging Sciences
Islamabad, Pakistan
June, 2025
2
Contents
1 Introduction 1
1.1 Problem Statement . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1
1.2 Motivation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
1.3 Problem Solution . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
1.4 Stake Holders . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
2 Project Description 5
2.1 Scope . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
2.2 Modules . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
2.2.1 Client Mobile App . . . . . . . . . . . . . . . . . . . . . . . . . 6
2.2.2 Admin Controls . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
2.2.3 Backend / AI Services . . . . . . . . . . . . . . . . . . . . . . . 6
2.3 Tools and Technologies . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
2.4 Work Division . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
2.5 TimeLine . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
References 11
3
List of Figures
4
List of Tables
2.1 Team Responsibilities . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
2.2 Table 2 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
0
Chapter 1
Introduction
The purpose of this project proposal is to define and present an AI powered preparation
assistant designed for Matric and FSc students in Pakistan, particularly those preparing
for board exams (FBISE) and entry tests (MDCAT, ECAT). The project aims to address
long standing challenges faced by students due to book constrained learning, limited personalization in exam preparation and manual exam topic predictions. Our proposed system leverages Natural Language Processing (NLP), machine learning, and Retrieval Augmented Generation (RAG) techniques to generate syllabus constrained questions, predict
high probability topics from past papers, and create personalized study plans. By combining AI driven content generation, predictive analytics, adaptive difficulty, this project
aspires to democratize quality exam preparation for FBISE students.
1.1 Problem Statement
Pakistani students preparing for Matric and Intermediate board exams face several interlinked challenges that limit their ability to study effectively. Teachers at academies and
tuition centers are unable to give individualized attention to every student, leaving weaker
learners behind. Students are forced into a rigid book constrained system where even
scientifically correct answers are penalized if they do not exactly match textbook phrasing. Teachers often rely on manual prediction of important topics by reviewing years of
past papers, a time consuming and error prone process that can miss hidden trends. Our
system addresses these issues by providing an AI based, syllabus grounded preparation
assistant that personalizes revision, adaptive difficulty for preparation, and predicts high
probability questions.
Existing tools provide partial support but leave significant gaps:
• Mindgrasp.ai – an AI assistant that summarizes documents and videos into notes,
but it does not generate exam-style questions grounded in Pakistani board syllabi
1
1. Introduction
[4].
• Edkasa – a Pakistani EdTech platform offering live and recorded classes, quizzes,
and study material; however, it relies on pre-made content and lacks AI-driven question generation or adaptive practice [1].
• MDCAT.ai (MIRA) – provides an AI chatbot with MCQs, progress tracking, and
explanations for MDCAT, but it is limited to medical entrance tests and cannot
handle board book-constrained requirements [3].
• Maqsad – offers live/recorded classes and quizzes for Matric and FSc students,
yet it focuses on video-based learning rather than predictive analytics or adaptive
revision [2].
• Prepai.io – an AI tool for teachers to generate quizzes and tests from content,
but it targets educators instead of providing a complete, student-centric preparation
ecosystem [5].
1.2 Motivation
The motivation for this project arises from the pressing need to modernize exam preparation in Pakistan. Each year, thousands of students invest time and money in tuition centers
and academies, yet their outcomes remain uncertain because preparation is not personalized or data driven. Students often memorize notes without actually understanding concepts, since the system rewards book specific wording rather than comprehension. Those
who cannot afford tuition centers are further disadvantaged due to lack of resources. The
success of AI driven learning platforms globally shows that intelligent tutoring systems
can close this gap, but local needs such as book constrained accuracy require a custom
solution. Our motivation is to build a system that empowers every student, regardless of
location or background, to access personalized, high quality exam preparation that aligns
strictly with their syllabus.
1.3 Problem Solution
To solve these challenges, we propose the development of an AI powered exam preparation assistant accessible through a mobile application. The solution leverages Retrieval
Augmented Generation (RAG) to generate questions strictly grounded in official textbooks and syllabi, ensuring compliance with board requirements. It will automatically
create MCQs, short questions, and long questions in line with paper patterns. A predictive analytics module will analyze past papers to identify recurring questions and high
2
1.4 Stake Holders
probability topics, giving students a data driven advantage. The system will also feature
an adaptive revision planner that adjusts to each student’s strengths and weaknesses, using
feedback loops to refine learning paths over time. Core objectives of the system include:
• Automate syllabus aligned question generation across different difficulty levels.
• Predict and visualize exam trends and high probability topics using past paper analysis.
• Provide adaptive learning through personalized revision planners.
• Enable offline first learning for students with limited connectivity.
• Incorporate feedback loops to improve prediction accuracy and adapt to individual
performance.
• Offer performance dashboards with insights, strengths, and weaknesses.
• Ensure engagement via gamification and exam simulations.
By combining these features, the project ensures students not only prepare more efficiently but also gain confidence in their readiness for exams.
1.4 Stake Holders
The key stakeholders for the project are:
• Students (Matric & FSc): Primary users who will use the system for exam preparation.
• Teachers & Tutors: Reviewers and validators of AI generated questions and explanations.
• Parents/Guardians: Supporters who encourage adoption and monitor progress.
• Board Authorities (FBISE, Provincial Boards): Providers of official syllabi,
exam patterns, and past papers.
• Textbook Publishers: Providers of updated editions of official textbooks.
3
Chapter 2
Project Description
2.1 Scope
PrepifyAI is an AI driven, syllabus constrained preparation platform aimed at Matric and
FSc students of FBISE. Its core purpose is to generate accurate, board specific practice
questions and provide data driven predictions of high probability topics while personalizing the learning experience. The system ingests official textbooks from Punjab, KPK, and
Federal boards, stores them in a vector database with board and version tags, and employs
Retrieval Augmented Generation (RAG) to create MCQs, short questions, and long form
questions strictly from the latest edition of each book. A prediction engine analyzes past
papers to detect trends and recurring topics, offering students a probability based list of
important areas to focus on. After each real exam cycle, actual papers are compared with
predicted topics to compute a “predictability score,” thereby creating a transparent feedback loop that continuously improves accuracy. An adaptive learning module monitors
student performance and dynamically adjusts revision plans: if a student repeatedly struggles or even fails despite adequate preparation, the system revises the schedule, increases
practice in weak areas, and recommends new strategies. Gamification features such as
points, streaks, and leaderboards keep students motivated, while detailed dashboards visualize strengths, weaknesses, and progress over time. For this phase, the scope is limited
to science subjects (Physics, Chemistry, Biology, Mathematics). Future extensions such
as additional subjects, other provincial boards, or university level exams remain outside
the current scope but can be integrated using the same architecture.
5
2. Project Description
2.2 Modules
2.2.1 Client Mobile App
Android/iOS hybrid application (Flutter) providing all student facing features.
1. User authentication and profile management.
2. AI generated syllabus aligned question bank (MCQs, short, long).
3. Adaptive revision planner with 360° feedback loop.
4. Past paper trend visualization and high probability topic predictions.
5. Performance dashboard with topic wise analytics.
6. Offline first capability with background sync.
7. Gamification: points, badges, and leaderboards.
2.2.2 Admin Controls
1. Upload new or revised textbooks for ingestion.
2. Validate and approve sample AI generated questions.
3. Monitor prediction accuracy vs. actual exam papers.
4. Manage user accounts and track overall system health.
2.2.3 Backend / AI Services
Central services powering both apps.
1. Retrieval Augmented Generation pipeline for question generation.
2. Past paper analytics and prediction engine.
3. Adaptive learning engine using recommendation algorithms.
4. Evaluation metrics computation (accuracy, precision/recall, predictability score).
6
2.3 Tools and Technologies
2.3 Tools and Technologies
• Programming: Python (FastAPI) for backend, React Native for mobile client
• Machine Learning & NLP: HuggingFace Transformers (T5/BERT), sentence transformers for embeddings, scikit learn for trend analysis, BERTopic for topic modeling.
• Database: PostgreSQL for relational data; Pinecone or FAISS for vector embeddings.
• OCR & Preprocessing: Tesseract OCR for scanned textbooks.
• Deployment: Docker containers on cloud (AWS/GCP) with CI/CD pipeline.
• Version Control & Collaboration: GitHub, GitHub Actions.
• Visualization: D3.js / Chart.js for prediction accuracy dashboards.
2.4 Work Division
Table 2.1: Team Responsibilities
Name Registration Responsibility / Module / Feature
Saif ur Rehman 22I-8767
• Core AI Question Engine & Knowledge
Base
• Book-constrained content parsing &
question generation
• Answer explanation models
Ameer Hamza 22I-2579
• Smart Analysis & Predictive Planning
• Past paper trend analysis
• Adaptive revision planner
Fizza Sarfraz 22I-0546
• Personalized Student Profile
• Adaptive Practice & Assessment
• Accessibility & Engagement
7
2. Project Description
2.5 TimeLine
8
2.5 TimeLine
Table 2.2: Table 2
Iteration Time frame Tasks/Modules
1 Sept - Oct 2025
• Data Collection & Model Exploration
• Backend API & Database Setup
• Trend Analysis & Prediction Model
• QnA Generation Model
• Offline Sync
• Frontend App Development
• Testing
2 Nov - Jan 2026
• Backend API & Database Setup
• Trend Analysis & Prediction Model
• QnA Generation Model
• API Integration
• Frontend App Development
• Offline Sync
• Testing
3 Feb - Apr 2026
• Trend Analysis & Prediction Model
• QnA Generation Model
• API Integration
• Adaptive Difficulty & Personalization
• Offline Sync
• Frontend App Development
• Testing & User Feedback
4 May 2026
• Performance Optimization
• Final Deployment & Demo
• Testing & User Feedback
9
Bibliography
[1] Edkasa. https://edkasa.com.
[2] Maqsad. https://www.maqsad.io.
[3] Mdcat.ai. https://www.mdcat.mdskool.com.
[4] Mindgrasp.ai. https://www.mindgrasp.ai.
[5] Prepai.io. https://www.prepai.io/us.
11
this is my final year project 
you have to do code and tell me how to make files abd don code

## Backend quickstart (local)

1. Ensure Python 3.12+ is available (`python3 --version`).
2. Install dependencies (adds binaries to `~/.local/bin`):
   - `pip3 install --user -r backend/requirements.txt`
   - `export PATH="$HOME/.local/bin:$PATH"`
3. Run the FastAPI service from the repo root:
   - `PYTHONPATH=backend uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload`
4. Verify the health endpoint in a browser or with curl:
   - `curl http://127.0.0.1:8000/api/health`
