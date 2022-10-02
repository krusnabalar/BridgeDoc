import streamlit as st

st.set_page_config(page_title="About", page_icon="📈")

st.title('About Project')

st.write("""

Inspiration
When was the last time you had an uncomfortable sensation that you didn’t know how to describe? You look it up on google, WebMD and ask onreddit, but find yourself just as uninformed and even more stressed than before. You end up calling a clinic or hospital to speak with a doctor, and find yourself having to wait a week until the next available appointment.

The general public is not trained to be aware of and describe the symptoms they might be going through. The way we describe our sensations can vary enormously, often we use idioms and other figures of speech. The stress and struggle of being unable to understand our body’s pain can be frustrating. Even in speaking with doctors, there’s often misunderstandings, and a lot of back and forth, until the doctor can finally understand the patient’s symptoms. In the field of medicine and healthcare, that kind of subjectivity and unpredictability can be dangerous, inefficient, and costly. 

That got our team to wonder: What if there’s a way to effectively predict a patient’s symptoms based on their own description in a fraction of the time at no cost to the patient?

BMJ Journal published a study which performed research on clinical text to extract mental health symptoms and using a classification NLP model, citing the automatability of the symptom detection process as being a credible way to approach this issue.
Solution
Introducting (project name), the tool that doctors and the general public can use to understand and identify their symptoms and diseases. (project name) will use classification tools provided by co:here to detect and identify the specific symptoms, for the knowledge of the doctor, and possible disease diagnoses, for the knowledge of the doctor and the patient.

It will allow an ease of communication between a doctor, clinic, or hospital with the patients by using a model trained with colloquial descriptions of symptoms to identify the likelihood of the patient’s symptoms.
Competitive Advantage
Companies like WebMD, Mayo Clinic, DearDoc, Mercury Healthcare all lack a way to enhance user inquiry and streamline the communication between doctors and patients. (project name) equips users and medical businesses to prevent the struggle and misunderstandings involved in translating a patient’s description of their issue and the doctor’s knowledge of what exactly those symptoms are, helping them efficiently pin point the most likely solutions. This has not been used in a professional medical sense for patients and can help edge over competitors in a significant way with a high quality symptom prediction model.
Revenue and Expenses
There are two B2B (doctors, hospitals) and B2C (online website clients) solution that (project name) provides. B2B solutions will be provided initially per user at a contract price based on the user report and needs of the doctor/hospital. B2C users will have free access. Expenses will be website hosting when moved to a different website that is more customized, as well as to access data that is more reliable by finding methods to get a secure access to it. Research expenses for improving model prediction will also be there.
Key Metrics
We will track the following key metrics
Growth: number of doctor contracts acquired per month, number of users accessing website
Engagement: use tools like Hotjar to track website interaction (user remains anonymous), track number of searches made per user
Marketing: to measure success for our marketing efforts, we will evaluate cost per acquisition, cost per clicks, and understanding the trends in impression to generate better marketing assets iteratively. We will also research marketing tacics of companies like Zocdoc who created an industry tool used by doctors.
Product: we will track and receive product feedback dynamically using tools like hotjar to understand user engagement with the product (what parts of the website are being used, how long they spend on the website, etc.
How We Built It
We built everything with python. Using jupyter notebooks we tested out co:here’s endpoints, integrated them into the boilerplate provided by LabLab and co:here. The app is deployed using streamlit. Data was collected from various tools such as reddit and google search scrapers, forums. To reach co:here’s requirement for a minimum of 250 examples to train the classify model, due to scarcity of data, we used co:here’s generate tool to build more examples by fine-tuning the model and using specific input phrases that generate reliable results.
What's next for (project name)
We would love to see (project name) to be a standalone tool that can be integrated with online tools for clinics and doctors with private practices, as well as hospital which often deal with issues of patient capacity limits, to automate the report creation by listing possible symptoms and diagnoses automatically. This would require adding a co:here-trained chat-bot that can extract the information from the user in a friendly, secure, and reliable way, similar to how a doctor might on the phone, and produce a report based on the user’s profile (gender, age, previous conditions, etc.) to improve the symptom and disease prediction.

Additionally, we leveraged insights from our mentor Ervin, and the “How to get funding from your startup” workshop by Pawel Czech and Mathias Asberg to understand business needs and identify the gaps in what’s currently being offered in our product. It’s important to focus our efforts to specific medical domains to improve accuracy, user retention, and help market and get clients. And the user base can expand by changing the architecture of our model to have a bigger tool that operates like the following:
Take input from user and classify what medical domain the query is in.
Based on the prediction confidence levels, use the top medical domains and send the user input to specialized classify models trained for the specific domain.
Get top predictions from those results of the symptoms as well as the disease.

This does not narrow down the user base, and more importantly, it provides improved symptom prediction and more reliable results. 
Challenges we ran into
One of the major challenges for the project was data collection. Due to the sensitive nature of the medical research, we struggled in getting access to corpuses and datasets available that would assist in building the data collection. With the lack of time and in some cases, legal roadblocks, we were unable to gather real patient data, which would have been much more insightful. We restored to using data online, which aligns with the nature of the tool (website), because the language people use for google searches and to communicate online is different from how they might speak to people offline.

Finetuning the generate model to produce varied and high-quality strings, but the documentation was quite helpful and were able to get good results.

Due to the limited customization options on streamlit we struggled with implementing styling to the website to improve the UI/UX.
Accomplishments that we're proud of
The amazing thing about this app is it’s able to work with a variety of colloquial language, a kind of flexibility that can be experienced by trying it out. And not only does it provide symptom predictions, it also does the disease diagnosis prediction function using NLP based on the possible symptoms, incorporating the functionality of websites like WebMD.

We’re proud to be able to use co:here’s models in such a challenging, creative, and complex way. Streamlit eased the deployment process by a huge margin and allowed us to focus on challenges we faced such as getting enough data to train the model.
What we learned
We witnessed, and were fortunate enough to contribute to the incredible progress happening in the NLP space. The transformer paper was released only 5 years ago, and in that time co:here has realized the potential of the field in incredible speed. It was insightful to understand the products co:here has built, and experience the flexibility and potential for their products by learning to work with them and understanding best practices. With the power this technology has, it can become an incredibly powerful tool for decision-making, conversation, data generation and visualization, creating and understanding code, and more.

Researching the medical problem-space, we found literature highlighting the problem of the patient-doctor communication gap. The friction and inefficiencies it can cause in the healthcare system was insightful in realizing that this is an important problem to solve. In today’s world with problems that humanity does not have the time, resources, and technology to solve, it’s truly inspiring to have companies like co:here to help us turn problems like that into ones that CAN be solved.
Built With
co:here Classify, co:here Generate, Python, Streamlit
Repo: https://github.com/krusnabalar/voyagers/
""")