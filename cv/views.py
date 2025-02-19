from django.shortcuts import render

def cv_view(request):
    context = {
        'name': "KAARTIKEYA PANJWANI",
        'phone': "+1-(667)325-7618",
        'email': "k.panjwani@nyu.edu",
        'website': "https://kaartikeya15.github.io/",
        'education': [
            {
                'institution': 'New York University, New York, NY',
                'degree': 'Master of Science, Computer Science',
                'date': 'May 2025'
            },
            {
                'institution': 'Vellore Institute of Technology, Tamil Nadu, India',
                'degree': 'Bachelor of Technology, Computer Science and Engineering',
                'date': 'Aug 2023'
            }
        ],
        'experience': [
            {
                'title': 'Software Developer',
                'company': 'NYU Courant Institute of Mathematical Sciences, New York, USA',
                'date': 'May 2024 – Present',
                'details': [
                    "Spearheading the development of the AI4Health website using React, HTML, Tailwind CSS, and WordPress",
                    "Collaborating with designers and backend developers to create seamless and visually appealing user interfaces",
                    "Implementing responsive design principles and dynamic content to ensure optimal performance across various devices and browsers",
                    "Conducting thorough code reviews and testing to uphold high standards of code quality and functionality",
                    "Utilizing project management tools to track progress and meet deadlines efficiently"
                ]
            },
            {
                'title': 'Web Development Project Lead',
                'company': 'Namhya Foods, Gurugram, India',
                'date': 'Jan 2021 – Jul 2023',
                'details': [
                    "Developed the website for the venture for their online market using HTML, CSS, Javascript, PHP and Shopify that increased their sales by 1.8x",
                    "Expanded my role as advisor to the development team and spearheaded the project, applying search engine optimization and social media marketing that increased the company’s market reach by 37%",
                    "Coordinated with the development team and mastered Shopify to create an online web store for the venture"
                ]
            }
        ],
        'projects': [
            {
                'title': 'Wi-Fi Hotspot Locator Web Application',
                'institution': 'New York University, New York, USA',
                'date': 'Sep 2023 – Dec 2023',
                'details': [
                    "Developed a Wi-Fi hotspot locator web application for the citizens of New York City using HTML, CSS, and JavaScript",
                    "Utilized React.js for the frontend to create a responsive and dynamic user interface",
                    "Implemented Node.js for the backend to handle server-side logic and API interactions",
                    "Integrated Google Maps API for geolocation services and map rendering, employing RESTful API principles"
                ]
            },
            {
                'title': 'NYC 311 Service Data Science Project',
                'institution': 'New York University, New York, USA',
                'date': 'Sep 2023 – Dec 2023',
                'details': [
                    "Integrated 34M 311-Service Requests with NYC DOITT ZipCode data for comprehensive analysis of spatial, temporal, numeric, categorical, and text features",
                    "Optimized resource allocation by developing a predictive model using regression analysis (Random Forest Regressor with 87.11% accuracy)",
                    "Implemented classification techniques with an XGBoost classifier (91.28% accuracy) for efficient handling of service requests"
                ]
            }
        ],
        'skills': {
            'Technical_Skills': "Web Development, Machine Learning, Application Development, Database Management, Data Analysis and Interpretation",
            'Programming_Languages': "Python, HTML, CSS, JavaScript, PHP, C, C++, R, Swift, MySQL",
            'Frameworks': "React JS, Django, NumPy, Pandas, Hadoop, NLTK, TensorFlow, PyTorch, SciPy, Scikit-Learn",
            'Other_Tools': "Google Colab, Jupyter, Android Studio, Xcode"
        }
    }
    return render(request, 'cv/cv.html', context)