def get_bot_response(user_input):
    user_input = user_input.lower()

    # Provide a menu of options
    if user_input in ["help", "menu", "options"]:
        return (
            "Hi! I can help you with the following topics:\n"
            "- Type 'technology' to hear the latest tech trends\n"
            "- Type 'career' for career advice\n"
            "- Type 'joke' if you'd like to hear a joke\n"
            "- Type 'nust hackathon' to learn about the NUST Annual Hackathon and its benefits\n"
            "- Type 'bye' to end the chat"
        )

    # Respond to specific topics
    elif "technology" in user_input:
        return "The latest in technology includes AI advancements, blockchain applications, and green tech innovations. Anything specific you'd like to discuss?"

    elif "career" in user_input:
        return "Career advice: Keep building your skills, network consistently, and pursue roles that align with your passions. Have any specific questions on careers?"

    elif "joke" in user_input:
        return "Why do programmers prefer dark mode? Because light attracts bugs! 😂"

    # NUST Hackathon and Specific Queries
    elif "nust hackathon" in user_input:
        return (
            "The NUST Annual Hackathon is a major event that fosters innovation, teamwork, and skill-building. "
            "Participants create solutions for real-world problems. Here are the available options for involvement:\n\n"
            "- **Type 'nust sponsor'** to learn about becoming a sponsor\n"
            "- **Type 'nust volunteer'** to learn about volunteering\n"
            "- **Type 'nust high school participant'** if you’re a high school student interested in joining\n"
            "- **Type 'nust university participant'** for university students who want to join\n\n"
            "Let me know which option interests you!"
        )

    # Sponsor Information
    elif "nust sponsor" in user_input:
        return (
            "As a sponsor for the NUST Annual Hackathon, you’ll get the opportunity to:\n"
            "- **Increase Brand Visibility**: Reach students, professionals, and educators across the tech community.\n"
            "- **Network with Talent**: Identify and engage with top emerging talent.\n"
            "- **Support Innovation**: Contribute to solutions addressing real-world issues.\n"
            "- **Benefit from Positive Branding**: Show your company’s support for education and community growth.\n\n"
            "Would you like to know more about sponsorship tiers or how to sign up?"
        )

    # Volunteer Information
    elif "nust volunteer" in user_input:
        return (
            "Volunteering at the NUST Annual Hackathon allows you to:\n"
            "- **Gain Event Experience**: Work behind the scenes of a large event.\n"
            "- **Build Leadership Skills**: Coordinate with teams and assist participants.\n"
            "- **Network**: Meet industry professionals and like-minded peers.\n\n"
            "Let me know if you'd like more details on how to volunteer or the tasks involved!"
        )

    # High School Participant Information
    elif "nust high school participant" in user_input:
        return (
            "High school students can participate in the NUST Annual Hackathon to:\n"
            "- **Experience Real-World Problem Solving**: Work on innovative projects.\n"
            "- **Learn New Skills**: Gain hands-on experience in coding and design.\n"
            "- **Network with University Students**: Engage with mentors and older students.\n\n"
            "Would you like more information on eligibility or how to register as a high school participant?"
        )

    # University Participant Information
    elif "nust university participant" in user_input:
        return (
            "University students participating in the NUST Annual Hackathon benefit by:\n"
            "- **Applying Classroom Knowledge**: Tackle real-world problems.\n"
            "- **Enhancing Career Prospects**: Build a portfolio of projects.\n"
            "- **Collaborating in Teams**: Gain experience working in teams.\n"
            "- **Accessing Internship Opportunities**: Connect with company representatives.\n\n"
            "Interested in joining? I can provide more information on the registration process or team formation!"
        )

    elif "bye" in user_input:
        return "Goodbye! Feel free to chat with me anytime."

    # Default response for unrecognized inputs
    else:
        return (
            "I'm here to help! You can type 'menu' to see what I can do, or ask about the NUST hackathon, "
            "technology, career advice, or request a joke."
        )
