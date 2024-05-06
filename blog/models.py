from django.db import models

# Create your models here.


class Post:
    def __init__(self, img_path, title, content, date):
        self.img_path = img_path
        self.title = title
        self.content = content
        self.date = date


# TODO will be removed
post_list = [
    Post('blog/images/chakra.jpg', 'CHAKRA ENERGIES', '''The human body receives, processes, and balances universal energies through energy centers known as chakras. Chakras help us balance our life energy and live at a higher level. However, over time, stress, emotional traumas, or negative energies can block or imbalance our chakras. This is where chakra cleansing comes into play.
The Importance of Chakra Cleansing
Chakra cleansing is a practice aimed at removing energy blockages when our energy centers are clogged or imbalanced. These blockages can lead to physical, emotional, or mental disturbances. With chakra cleansing, you can revitalize your energy flow, boost your life energy, and increase inner peace.
The Power of Natural Stones
Natural stones have been known for their healing and energizing properties for thousands of years. Each stone has its unique energy and frequency, which can help balance our chakras. Here are some stones and their effects on the chakras:
Red Jasper: Strengthens the root chakra, provides grounding.
Tourmaline: Cleanses and balances all chakras.
Rose Quartz: Opens the heart chakra, gives energy of love and compassion.
Lapis Lazuli: Activates the third eye chakra, increases insight.
How to Perform Chakra Cleansing?
Preparation: Create a comfortable environment, play soothing music, and take a relaxed position.
Select Natural Stones: Choose appropriate natural stones based on your needs.
Meditation: Close your eyes, take deep breaths, and place the stones on your chakras.
Feel the Energy Flow: Feel the energies of the stones and notice the resolution of blocked or imbalanced energies.
Gratitude: At the end of the meditation, express gratitude to the stones and the universe.
Conclusion
Chakra cleansing, combined with the healing energies of natural stones, is a wonderful way to balance your body, mind, and spirit. By practicing this regularly, you can boost your life energy, increase inner peace, and lead a healthier life.''', '2021-01-01'),

    Post('blog/images/positive-energy.jpg', 'Energy Cleansing and Elevation with Incense', '''The Most Powerful Incenses and Their Uses
Incense has been used for thousands of years for rituals, meditation, and energy cleansing purposes. We can benefit from the unique scents and energies of incense to cleanse negative energy from our environment, elevate positive energy, and spread it around. Here are the power, uses, and benefits of various incenses:
1. White Sage
Usage: Burn white sage leaves and spread its smoke around the area.
Benefits: Cleanses negative energy, elevates energy, and creates a protective shield.
2. Palo Santo
Usage: Light Palo Santo wood and spread its smoke around you.
Benefits: Attracts positive energy, provides emotional balance, and prepares the mind for meditation.
3. Lavender
Usage: Burn lavender flowers to create a light smoke.
Benefits: Has a calming, soothing, and stress-reducing effect.
4. Frankincense
Usage: Burn frankincense resin and spread its smoke.
Benefits: Strengthens spiritual connection, deepens meditation, and balances energy.
5. Copal
Usage: Light copal resin and spread its smoke around.
Benefits: Cleanses negative energy, clears the mind, and elevates positive energy.
How to Use?
Preparation: Create a comfortable environment, play soothing music, and take a relaxed position.
Incense Selection: Choose the appropriate incense based on your needs.
Burning: Light the incense and spread its smoke around you.
Meditation: Relax with the effect of the smoke, take deep breaths, and feel the positive energy.
Gratitude: At the end of the ritual, express gratitude to the incense and the universe.
Conclusion
Incense is a wonderful tool for energy cleansing and elevation. By choosing the right incense, applying the ritual correctly, and approaching with intention, you can transform the energy around you, elevate positive energy, and bring balanced energy into your life.
''', '2021-01-01'),

    Post('blog/images/aksesuar.png', 'Tree of Life Wall Accessories', '''The Tree of Life is considered a symbol of the universe, nature, and life in many cultures. This powerful symbol can bring positive energy and balance to your home or workplace. Here's information about the benefits of Tree of Life wall accessories and how they can be used:
Benefits:
Elevating Energy: The Tree of Life symbol attracts positive energy and revitalizes your space.
Balance and Harmony: The Tree of Life represents the balance and harmony of nature, which can help create a sense of balance and peace in your surroundings.
Spiritual Connection: The Tree of Life can strengthen your connection with the universe, nature, and your inner self.
Visual Richness: As a decorative touch, Tree of Life wall accessories add character to your space and provide visual richness.
How to Use?
Placement: Hang your Tree of Life wall accessory in a place where energy flow is strong, such as near your living room or workspace.
Setting Intentions: Set positive intentions while hanging the accessory; these intentions can enhance the energy of the Tree of Life.
Maintenance and Cleaning: Regularly clean your wall accessory and occasionally keep it under the sun or moonlight to refresh its energy.
Combinations: Combine the Tree of Life wall accessory with other energy-cleansing and balancing objects to create different energy combinations.
Conclusion
Tree of Life wall accessories can be a wonderful way to elevate energy and balance in your home or workplace. When hung in the right place, cared for regularly, and used with positive intentions, the Tree of Life symbol can add a positive touch to your life, enhancing inner peace and balance.''', '2021-01-01'),

    Post('blog/images/incense.jpg', 'Positive Energy', '''Positive Energy and Spiritual Energy: Meanings, Differences, and How to Elevate Them
Positive energy and spiritual energy play significant roles in our lives, greatly influencing our inner peace, balance, and quality of life. Here's information about the meanings, differences, and ways to elevate these two types of energy:
Positive Energy:
Meaning: Positive energy represents positive emotions and frequencies such as optimism, love, joy, and hope.
Benefits: Positive energy helps us be happier, more balanced, and productive. It can also reduce stress, increase mental clarity, and enhance the quality of life.
How to Elevate: You can elevate your positive energy by nourishing yourself with positive thoughts, proper nutrition, practicing meditation, spending time with loved ones, and spending time in nature.
Spiritual Energy:
Meaning: Spiritual energy is related to spiritual consciousness, deep insight, connection, and the quest for meaning.
Benefits: Spiritual energy can enhance spiritual growth, wholeness, and our capacity to understand the deeper meanings of life. It can also strengthen inner peace, wholeness, and a sense of purpose.
How to Elevate: Spiritual practices such as meditation, yoga, rituals, and devotion are wonderful ways to strengthen inner connection and elevate spiritual energy.
Difference Between Positive and Spiritual Energy:
While positive energy typically deals with positive emotions and frequencies related to daily life, spiritual energy is more concerned with deeper connection, quest for meaning, and inner growth.
Conclusion:
Positive energy and spiritual energy are two important types of energy that influence different aspects of our lives. Nourishing and elevating these two energies in a balanced way can help us lead a healthy, happy, and meaningful life. With the right activities, intentions, and commitment to practice, we can establish a deeper connection with these two types of energy and make positive changes in our lives.''', '2021-01-01'),
]
