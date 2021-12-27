
label lamp_visit_back_to_jafar:
    # $ skip_next = "skip_to_main"
    scene bg lib
    with dissolve
    show jaf normal
    with dissolve
    show jaf probing
    jaf "Done already?"
    abd "Well..."
    "..."
    show jaf normal
    jaf "Alright, you don't want to tell and I don't want to know."
    jaf "Let's move on."
    jaf "I've devised a fool-proof plan. "
    jaf "And just to be clear, by \"fool\" I mean you."
    jaf "After some education, the fool will infiltrate the palace and push the enemy to desperation."
    jaf "He will expose the rotten core of Agrabah's current rulers for everyone to see."
    show jaf smile
    jaf "And then...{w=.25} he will deliver the ultimate humiliation."
    abd "Can you stop talking about me in third person, Jafar? I'm standing right here. And I think I should feel insulted."
    show jaf thinking
    jaf "Hmmm, I guess a controlling a commoner in the palace will be harder than I thought."
    show jaf normal
    abd "Do you mean me?"
    jaf "Yes, of course. It will be hard, but I'm sure I can pull it off. You'll be fine."
    jaf "More than fine, in fact. You might find pleasure in it."
    abd "Heheheh, pleasure is good. I'm listening."
    jaf "Ah yes. Pleasure."
    show jaf thinking
    jaf "The ultimate goal. The driving force of nature. Better than all the wealth in the world."
    abd "I don't think any pleasure can top all the wealth in the world, Jafar."
    show jaf normal
    jaf "It would, you just don't understand it yet."
    jaf "In time, you will."
    show jaf thinking
    jaf "I'll have to write a book on that as well."
    show jaf normal
    jaf "Anyways, when you have a chance to go in that palace, you're going to have to look the part."
    jaf "First, you need to make some money to buy clothing."
    abd "Can't you give me some money or the clothing with magic? I thought Genies could use all sorts of little magic to help out."
    jaf "Of course I can, I have absolute power! The universe is mine to command and all of that jazz."
    jaf "But that might count as your wish. Like I said, I screwed up last time, and this time I want to do it right."
    jaf "The rules seem arbitrary."
    jaf "I don't want to take any risks on things that aren't important until I have a better sense of how these cosmic pencil pushers have set things up."
    abd "Good point, I would never think that far ahead. No wonder you became a Vizier."
    show jaf smile
    jaf "Yes, yes, I'm amazing. Now listen to me."
    show jaf normal
    jaf "You need to establish yourself as a wise man, solving people's problems."
    jaf "Once you're known for holding a solution to every problem, you can easily enter the palace."
    jaf "In my absence, and with my help, you will have no problem establishing yourself as a person of importance."
    abd "Like Malik and Hosein?"
    show jaf thinking
    jaf "I almost forgot about those two rats. They are an obstacle. We'll need to get rid of them too."
    show jaf normal
    jaf "So I guess that's everything: Your mission, wealth, your attire and combat training. Did I miss anything?"
    abd "Well...{w=.4} food...{w=.4} I'm starving."
    jaf "Ah yes, that too."
    jaf "Let us get out here and start executing our plan."
    abd "You mean..."

default cash_in_hand = quest(
    _("Cash in hand"),
    [_("We need 2000 dinars for some jewelry Jafar wants to order.")]
)

label lamp_visit_back_to_agrabah:
    scene black
    show bg agrabah with Dissolve(2)
    with dissolve
    show jaf normal
    with dissolve
    abd "... Your plan?"
    jaf "You're a part of it, that makes it our plan."
    show jaf thinking
    jaf "Anyways, you might need quick access to the jars room though., now let me see."
    show jaf normal
    jaf "You can't carry the lamp around, knowing you, you'll lose it in a day."
    show jaf thinking
    jaf "I think I know what to do, you need to come up with some serious money for that though."
    show jaf normal
    jaf "2000 should suffice."
    $ qlog.got(cash_in_hand)
    abd "2000?{w=.4} how?."
    jaf "Come up with something,{w=.2} off you go.{w=.2} I'll be in the lamp if you need me."
    
    jump agrabah
