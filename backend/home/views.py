from rest_framework.decorators import api_view
from rest_framework.response import Response
@api_view(['GET'])
def homepage(request):
    data = {
        "title": "Welcome to our travel agency!",
        "text": "Бажаєте вирушити у довгоочікувану літню відпустку? Чи можливо відсвяткувати Новий Рік на узбережжі Індійського океану? Туристична агенція 'Make Travel' пропонує варіанти відпочинку на будь-який смак та бюджет! Наші менеджери допоможуть підібрати та оформити тур відповідно до Ваших побажань, оформлять усі документи, а Вам залишиться лише зібрати валізи та вирушити у незабутню подорож!",
        "featured_destinations": ["Italy", "France", "Spain", "Ibiza"],
        "contact_email": "info@travelagency.com",
        "testimonials": [
            {"name": "John Doe", "feedback": "Amazing service! We had a great time in Spain."},
            {"name": "Jane Smith", "feedback": "The trip to Ibiza was a dream come true. Highly recommended!"}
        ]
    }
    return Response(data)


@api_view(['GET'])
def about_page(request):
    data = {
        "about": "We are a travel agency committed to delivering the best travel experiences. Whether you're looking for a relaxing beach getaway or an adventurous trek through the mountains, we have options for every taste and budget.",
        "services": [
            "Customized travel packages",
            "Hassle-free bookings",
            "24/7 customer support",
            "Travel insurance and visa assistance",
            "Group and family travel discounts"
        ],
        "team": [
            {"name": "Alice Brown", "role": "CEO", "bio": "Alice has over 10 years of experience in the travel industry."},
            {"name": "Bob Green", "role": "Tour Manager", "bio": "Bob is passionate about curating unique travel experiences for clients."}
        ]
    }
    return Response(data)


@api_view(['GET'])
def contact_page(request):
    data = {
        "contact_info": {
            "email": "info@travelagency.com",
            "phone": "+123456789",
            "address": "123 Travel Street, Wanderlust City, 56789",
        },
        "support_hours": "Monday to Friday, 9 AM to 5 PM",
        "location": {
            "latitude": 40.712776,
            "longitude": -74.005974
        },
        "social_media": {
            "facebook": "https://facebook.com/MakeTravelAgency",
            "instagram": "https://instagram.com/MakeTravelAgency",
            "twitter": "https://twitter.com/MakeTravelAgency"
        }
    }
    return Response(data)
