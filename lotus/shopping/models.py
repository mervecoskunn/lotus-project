from django.db import models

# Create your models here.
cat_bracelet = 'bracelet'
cat_chackra_stone = 'chakra-stones'
cat_incense = 'incence'
cat_natural_stone = 'natural-stones'
cat_pandul = 'pendulum'


class Product:
    def __init__(self, id, name, price, category, description, rating=0, img_path=""):
        self.id = id
        self.name = name
        self.price = price
        self.category = category
        self.description = description
        self.rating = rating
        self.img_path = img_path

    def __str__(self):
        return '[' + self.name + ' ' + str(self.price) + ' ' + self.description + ' ' + str(self.rating) + ']'


product_list = [
    Product(id=1, name='Chakra Bracelet', price=15, category=cat_bracelet,
            description="Designed to balance our energy centers and enhance inner harmony, this bracelet targets the seven main chakra points. Combining the power of natural stones and crystals, this bracelet helps boost your life force, supporting mental and emotional equilibrium. Each unique stone's energy works in harmony with the chakras in your body, optimizing your energy flow and contributing to an elevated quality of life",
            rating=5, img_path="shopping/images/products/bracelet/chackra_bracelet.jpg"),

    Product(id=2, name='Amethyst Natural Stone Bracelet', price=10, category=cat_bracelet,
            description="""Elevate your style and energy with our Amethyst Natural Stone Bracelet. Known as a stone of spiritual growth and protection, amethyst offers a range of benefits for both the mind and body. Benefits of Amethyst:
            ⦁	Spiritual Growth: Amethyst is often associated with spiritual awareness, inner peace, and higher consciousness. It can help you connect with your intuition and enhance spiritual practices.
            ⦁	Emotional Balance: This calming stone is believed to soothe irritability, balance mood swings, and dispel negative emotions, promoting emotional well-being.
            ⦁	Protection: Amethyst is considered a protective stone that wards off negative energies and psychic attacks, creating a shield of spiritual light around the body""", rating=4.8, img_path="shopping/images/products/bracelet/ametist_bracelet.jpeg"),

    Product(id=3, name='Rose Quartz Natural Stone Bracelet',
            price=10, category=cat_bracelet, description="""Rose Quartz Natural Stone Bracelet
Infuse your style with love and compassion through our Rose Quartz Natural Stone Bracelet. Known as the "stone of unconditional love," rose quartz carries a gentle, soothing energy that encourages self-love, compassion, and harmony.
Benefits of Rose Quartz:
⦁	Unconditional Love: Rose quartz is associated with the heart chakra and is believed to open the heart to all types of love, fostering empathy, forgiveness, and compassion.
⦁	Emotional Healing: This calming stone helps to release emotional wounds, reduce stress, and bring a sense of calmness and inner peace.
⦁	Harmony and Balance: Rose quartz promotes harmony and balance in relationships, enhancing communication, understanding, and mutual respect""", rating=5, img_path="shopping/images/products/bracelet/rose_quartz_bracelet.jpg"),

    Product(id=4, name='LAPIS CHAKRA STONE', price=10, category=cat_chackra_stone, description="""Lapis Lazuli for Throat Chakra: Enhance Communication and Self-Expression
Lapis Lazuli is a powerful crystal known for its deep blue color and potent energy, making it an excellent stone for activating and balancing the Throat Chakra. Located at the base of the throat, the Throat Chakra is associated with communication, self-expression, and speaking one's truth.
Benefits of Using Lapis Lazuli for Throat Chakra:
⦁	Enhances Communication: Lapis Lazuli stimulates the Throat Chakra, enhancing communication skills, and promoting clear and honest expression of thoughts and feelings.
⦁	Supports Self-Expression: By activating the Throat Chakra, Lapis Lazuli encourages self-expression, creativity, and the ability to articulate one's ideas and emotions.
⦁	Promotes Truth and Integrity: Lapis Lazuli helps to align the Throat Chakra, promoting honesty, integrity, and the courage to speak and live your truth.
How to Use Lapis Lazuli for Throat Chakra:
⦁	Wear as Jewelry: Wear Lapis Lazuli as a necklace or pendant to keep it close to the Throat Chakra, allowing its energy to flow directly to this energy center.
⦁	Meditation: Hold Lapis Lazuli in your hand or place it on your throat area during meditation to focus on balancing and activating the Throat Chakra.
⦁	Incorporate into Daily Life: Carry Lapis Lazuli with you or place it in your living or work space to benefit from its energy throughout the day, enhancing communication and self-expression.
Enhance communication, support self-expression, and promote truth and integrity by incorporating the powerful energy of Lapis Lazuli into your Throat Chakra balancing practices.""", rating=4.5, img_path="shopping/images/products/chackra_stone/lapis-chakra.png"),

    Product(id=5, name='CROWN CHAKRA STONE - LABRADORITE', price=10,
            category=cat_chackra_stone, description="""Labradorite for Crown Chakra: Connect to Higher Consciousness and Spiritual Wisdom
Labradorite is a captivating gemstone known for its stunning play of colors and powerful mystical properties. As a stone that resonates strongly with the Crown Chakra, Labradorite is instrumental in facilitating spiritual growth, connecting to higher realms of consciousness, and enhancing overall well-being.
Benefits of Using Labradorite for Crown Chakra:
⦁	Facilitates Spiritual Growth: Labradorite activates and balances the Crown Chakra, facilitating spiritual growth, enlightenment, and a deeper connection to your higher self and the universe.
⦁	Enhances Intuition and Insight: By stimulating the Crown Chakra, Labradorite enhances intuition, insight, and psychic abilities, allowing you to tap into higher wisdom and guidance.
⦁	Promotes Balance and Harmony: Labradorite's balancing energy helps to harmonize the Crown Chakra, promoting a sense of balance, peace, and spiritual well-being.
How to Use Labradorite for Crown Chakra:
⦁	Meditation: Hold Labradorite in your hand or place it on the Crown Chakra (located at the top of the head) during meditation to focus on balancing and activating this energy center.
⦁	Wear as Jewelry: Wear Labradorite as a necklace or crown to keep its energy close to your Crown Chakra, benefiting from its spiritual-enhancing properties throughout the day.
⦁	Incorporate into Daily Life: Carry Labradorite with you or place it in your living or work space to benefit from its energy, promoting spiritual growth, enhancing intuition, and fostering a deeper connection to higher consciousness.
Connect to higher consciousness, enhance spiritual growth, and tap into intuitive wisdom by incorporating the transformative energy of Labradorite into your Crown Chakra balancing and spiritual practices.""", rating=5, img_path="shopping/images/products/chackra_stone/crown-chakra.png"),

    Product(id=6, name='CROWN CHAKRA STONE - AMETHYST', price=10,
            category=cat_chackra_stone, description="""Amethyst for Crown Chakra: Enhance Spiritual Connection and Inner Wisdom
Amethyst is a cherished gemstone revered for its stunning purple hue and powerful spiritual properties. As a stone closely associated with the Crown Chakra, Amethyst is invaluable for enhancing spiritual connection, deepening meditation, and fostering inner wisdom and enlightenment.
Benefits of Using Amethyst for Crown Chakra:
⦁	Enhances Spiritual Connection: Amethyst activates and aligns the Crown Chakra, facilitating a stronger connection to higher realms, spiritual guides, and your higher self.
⦁	Promotes Inner Wisdom and Enlightenment: By stimulating the Crown Chakra, Amethyst encourages introspection, enhances intuition, and fosters inner wisdom and enlightenment.
⦁	Supports Meditation and Mindfulness: Amethyst's calming energy helps to deepen meditation, promote mindfulness, and create a serene and peaceful state of mind.
How to Use Amethyst for Crown Chakra:
⦁	Meditation: Hold Amethyst in your hand or place it on the Crown Chakra (located at the top of the head) during meditation to focus on balancing and activating this energy center.
⦁	Wear as Jewelry: Wear Amethyst as a necklace or bracelet to keep its energy close to your Crown Chakra, benefiting from its spiritual-enhancing properties throughout the day.
⦁	Incorporate into Daily Life: Carry Amethyst with you or place it in your living or work space to benefit from its energy, enhancing spiritual connection, promoting inner wisdom, and fostering a deeper sense of peace and serenity.
Enhance spiritual connection, foster inner wisdom, and deepen meditation by incorporating the transformative energy of Amethyst into your Crown Chakra balancing and spiritual practices.
""", rating=5, img_path="shopping/images/products/chackra_stone/crown-chakra-ametist.png"),

    Product(id=7, name='CHAKRA INCENCE', price=15, category=cat_incense, description="""Chakra Incense: Harmonize Your Energy Centers
Experience the transformative power of Chakra Incense, meticulously crafted to align and balance your body's energy centers, known as chakras. Each incense stick is infused with pure essential oils, herbs, and resins specifically chosen to resonate with each chakra, promoting harmony, balance, and well-being.
Benefits of Using Chakra Incense:
⦁	Aligns and Balances Chakras: Chakra Incense helps to align and balance the seven main chakras, promoting overall energy harmony and balance within the body.
⦁	Promotes Relaxation and Inner Peace: The soothing aroma of Chakra Incense helps to calm the mind, reduce stress, and promote relaxation and inner peace.
⦁	Enhances Meditation and Spiritual Connection: Burning Chakra Incense during meditation or spiritual practices can deepen your connection to your higher self, enhance intuition, and elevate your spiritual journey.
How to Use Chakra Incense:
⦁	During Meditation or Yoga: Burn Chakra Incense before or during meditation or yoga practices to enhance focus, deepen relaxation, and align your energy centers.
⦁	In Sacred Spaces: Use Chakra Incense to cleanse and purify sacred spaces, creating a harmonious and uplifting environment for spiritual practices.
⦁	For Daily Well-being: Incorporate Chakra Incense into your daily routine to promote balance, harmony, and overall well-being.
Elevate your spiritual journey, align your energy centers, and infuse your space with harmony and balance by incorporating Chakra Incense into your daily rituals and practices""", rating=1.5, img_path="shopping/images/products/incence/chakra_incence.webp"),

    Product(id=8, name='SANTA PALO INCENCE', price=12, category=cat_incense,
            description="""Santa Palo Incense: Purify and Energize Your Space
Discover the sacred and purifying aroma of Santa Palo Incense, crafted from the sacred wood of the Palo Santo tree. Revered for centuries for its cleansing and healing properties, Santa Palo Incense is perfect for purifying your space, enhancing meditation, and promoting overall well-being.
Benefits of Using Santa Palo Incense:
⦁	Purifies and Cleanses: Santa Palo Incense has powerful cleansing properties that help to clear negative energies, purify your space, and create a sacred and harmonious environment.
⦁	Enhances Meditation and Focus: The soothing and grounding aroma of Santa Palo Incense helps to enhance meditation, deepen focus, and promote a calm and centered state of mind.
⦁	Promotes Relaxation and Well-being: Burning Santa Palo Incense can help reduce stress, anxiety, and promote relaxation, creating a tranquil and peaceful atmosphere conducive to healing and well-being.
How to Use Santa Palo Incense:
⦁	During Meditation or Yoga: Burn Santa Palo Incense before or during meditation or yoga practices to cleanse your space, enhance focus, and deepen your spiritual connection.
⦁	For Daily Cleansing: Use Santa Palo Incense daily to purify your home, office, or any space, removing negative energies and promoting a positive and harmonious environment.
⦁	As a Ritual Tool: Incorporate Santa Palo Incense into your rituals or ceremonies to cleanse, purify, and prepare your space for spiritual practices or ceremonies.
Elevate your spiritual practices, purify your space, and promote overall well-being by incorporating the sacred and purifying aroma of Santa Palo Incense into your daily rituals and practices""", rating=3.5, img_path="shopping/images/products/incence/santa-palo-incence.webp"),

    Product(id=9, name='JASMINE INCENCE', price=14, category=cat_incense,
            description="""Jasmine Incense: Elevate Your Senses and Spirit
Immerse yourself in the enchanting aroma of Jasmine Incense, known for its sweet, floral fragrance that captivates the senses and uplifts the spirit. Made from the pure essence of Jasmine flowers, this incense is perfect for enhancing relaxation, promoting positivity, and creating a romantic and soothing atmosphere.
Benefits of Using Jasmine Incense:
⦁	Uplifts and Inspires: The sweet and floral aroma of Jasmine Incense has a rejuvenating effect that uplifts the spirit, inspires creativity, and promotes a sense of well-being.
⦁	Promotes Relaxation and Calm: Jasmine Incense has a calming and soothing effect that helps to reduce stress, anxiety, and tension, creating a peaceful and harmonious environment.
⦁	Enhances Romance and Sensuality: The romantic and sensual aroma of Jasmine Incense can enhance romance, intimacy, and create a warm and inviting atmosphere perfect for romantic evenings or special occasions.
How to Use Jasmine Incense:
⦁	For Relaxation and Meditation: Burn Jasmine Incense during meditation, yoga, or relaxation practices to promote a calm and peaceful state of mind, and enhance focus and concentration.
⦁	For Romance and Special Occasions: Use Jasmine Incense to create a romantic and sensual atmosphere for special occasions, romantic evenings, or intimate gatherings.
⦁	For Daily Well-being: Incorporate Jasmine Incense into your daily routine to uplift your mood, enhance positivity, and create a serene and harmonious environment at home or work.
Elevate your senses, promote relaxation, and infuse your space with the enchanting and uplifting aroma of Jasmine Incense by incorporating this beautiful incense into your daily rituals and practices.""", rating=3.6, img_path="shopping/images/products/incence/jasmine-incence.jpeg"),

    Product(id=10, name='AMETHYST NATURAL STONE', price=50, category=cat_natural_stone,
            description="""Amethyst is one of the most recognized and beloved natural stones. With its captivating shades of purple, this stone not only offers aesthetic elegance but also helps balance energy in your environment.
Benefits of Using Amethyst in Your Space:
⦁	Reduces Stress and Anxiety: Amethyst has a calming and soothing energy. When used in your space, it can reduce stress, calm the mind, and alleviate anxiety.
⦁	Brings Balance and Harmony: Amethyst helps balance energy centers and brings peace and harmony to the environment. This can enhance your inner peace and overall quality of life.
⦁	Promotes Creativity and Innovation: Amethyst is a stone that encourages creativity and innovation. When used in workspaces or studios, it can boost creativity and productivity.
How to Use Amethyst Natural Stone in Your Space:
⦁	At Home: Place Amethyst clusters or geodes in living rooms, bedrooms, or meditation spaces to promote a calming and peaceful atmosphere.
⦁	In Workspaces: Keep Amethyst stones on your desk or workspace to reduce stress, enhance creativity, and improve focus.
⦁	In Meditation or Yoga Spaces: Place Amethyst stones around your meditation or yoga space to create a serene and balanced environment for spiritual practices.
Elevate your living or workspace, enhance your well-being, and tap into the calming and balancing energy of Amethyst by incorporating this beautiful natural stone into your environment""", rating=5, img_path="shopping/images/products/natural_stone/ametist.jpeg"),

    Product(id=11, name='CITRINE NATURAL STONE', price=55, category=cat_natural_stone,
            description="""Using Citrine Natural Stone in Your Space
Citrine is a radiant and energizing natural stone known for its golden hues and positive energy. Incorporating Citrine into your environment can bring warmth, prosperity, and uplifting energy to your space.
Benefits of Using Citrine in Your Space:
⦁	Attracts Abundance and Prosperity: Citrine is often referred to as the "Merchant's Stone" due to its reputation for attracting wealth, success, and abundance. Placing Citrine in your space can help manifest prosperity and opportunities.
⦁	Boosts Positive Energy: Citrine radiates a cheerful and optimistic energy that can uplift spirits, dispel negativity, and promote a positive outlook on life.
⦁	Enhances Creativity and Confidence: Citrine stimulates creativity, boosts self-confidence, and encourages personal empowerment, making it an ideal stone for artists, entrepreneurs, and anyone pursuing their passions.
How to Use Citrine Natural Stone in Your Space:
⦁	At Home: Display Citrine clusters or tumbled stones in the living room, home office, or wealth corner (southeast) of your space to attract abundance and prosperity.
⦁	In Workspaces: Place Citrine stones on your desk or workspace to stimulate creativity, enhance focus, and boost productivity.
⦁	In Meditation or Yoga Spaces: Incorporate Citrine into your meditation or yoga practice by placing it near your mat or meditation area to uplift your energy and promote positivity.
Elevate your living or workspace, attract prosperity, and infuse your environment with the uplifting and energizing energy of Citrine by incorporating this beautiful natural stone into your space""", rating=2.8, img_path="shopping/images/products/natural_stone/citrine-stone.jpeg"),

    Product(id=12, name='TURQUOISE NATURAL STONE ', price=35, category=cat_natural_stone,
            description="""Using Turquoise Natural Stone in Your Space
Turquoise is a captivating natural stone known for its vibrant blue-green hues and protective energies. Incorporating Turquoise into your environment can bring a sense of calm, protection, and positive energy to your space.
Benefits of Using Turquoise in Your Space:
⦁	Promotes Calmness and Protection: Turquoise is a stone of tranquility and protection. Placing Turquoise in your space can help create a calming and protective atmosphere, shielding you from negative energies.
⦁	Enhances Communication and Self-Expression: Turquoise stimulates the throat chakra, promoting clear communication, self-expression, and confidence in expressing your thoughts and feelings.
⦁	Attracts Positivity and Well-being: Turquoise radiates positive energy and encourages emotional balance, helping to uplift spirits, reduce stress, and promote overall well-being.
How to Use Turquoise Natural Stone in Your Space:
⦁	At Home: Display Turquoise clusters, tumbled stones, or decorative items in communal areas like the living room or dining room to promote a harmonious and protective environment.
⦁	In Workspaces: Keep Turquoise stones on your desk or workspace to enhance communication, boost creativity, and foster a positive and productive work environment.
⦁	In Meditation or Yoga Spaces: Incorporate Turquoise into your meditation or yoga practice by placing it near your mat or meditation area to enhance your spiritual connection, promote calmness, and uplift your energy.
Elevate your living or workspace, promote calmness and protection, and infuse your environment with the soothing and protective energy of Turquoise by incorporating this beautiful natural stone into your space.""", rating=5, img_path="shopping/images/products/natural_stone/turquaz_natural_stone.webp"),

    Product(id=13, name='Crystal Quartz Pendulum', price=20, category=cat_pandul,
            description="""Unlock the mysteries of the universe and tap into your intuitive abilities with our Crystal Quartz Pendulum. Known as the "master healer," crystal quartz is a versatile and powerful stone that amplifies energy, clarity, and intention.
Benefits of Crystal Quartz Pendulum:
⦁	Enhanced Intuition: Crystal quartz pendulum helps to enhance your intuitive abilities and connect with your higher self, guiding you towards answers and insights.
⦁	Clarity and Focus: This clear quartz variety promotes mental clarity, focus, and concentration, making it a valuable tool for meditation, divination, and spiritual growth.
⦁	Amplifies Energy: Crystal quartz acts as an energy amplifier, enhancing the effects of other stones and balancing your energy centers for improved vitality and well-being.""", rating=4.7, img_path="shopping/images/products/pandul/kristal_quartz_pandul.webp"),

    Product(id=14, name='Pink Quartz Pendulum', price=20, category=cat_pandul,
            description="""Enhance your intuition and embrace unconditional love with our Pink Quartz Pendulum. Known as the "stone of unconditional love," pink quartz carries a gentle, soothing energy that encourages self-love, compassion, and harmony.
Benefits of Pink Quartz Pendulum:
⦁	Unconditional Love: Pink quartz pendulum promotes unconditional love, compassion, and empathy, helping you to open your heart to love and embrace self-acceptance.
⦁	Enhanced Intuition: This beautiful stone helps to enhance your intuitive abilities, allowing you to connect with your inner wisdom and intuition more deeply.
⦁	Emotional Healing: Pink quartz supports emotional healing, reducing stress, anxiety, and emotional turmoil, and promoting inner peace, serenity, and overall emotional well-being.""", rating=4.2, img_path="shopping/images/products/pandul/pink_quartz_pendulum.jpeg"),

    Product(id=14, name='Brass Pendulum', price=20, category=cat_pandul,
            description="""Brass Pendulum
Discover the art of divination and explore your intuitive abilities with our Brass Pendulum. Made from high-quality brass, this pendulum combines timeless elegance with practical functionality.
Benefits of Brass Pendulum:
⦁	Practical and Durable: Brass is known for its durability and practicality, making it an excellent material choice for pendulums that are used frequently for divination and spiritual practices.
⦁	Balancing and Harmonizing: Brass has a balancing and harmonizing energy that helps to align and balance your energy centers, promoting overall well-being and harmony.
⦁	Versatile and Easy to Use: Our brass pendulum is versatile and easy to use, making it suitable for both beginners and experienced practitioners alike.""", rating=5, img_path="shopping/images/products/pandul/brass_pendulum.jpeg"),

]
