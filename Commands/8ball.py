from random import randint

outputs = ['Yes.', 'No.','Perhaps.','Maybie.','The answer is cloudy ask later...',
    'You know it.','That is a bunch of gibberish!', 'Nonsence!',
    'What are you thinking of course it is yes!', 'What are you thinking of course it is no!',
    'Indeed.','Negative.','Why are you asking me? I don\'t know.',
    'I think you know what the answer is.','Is 1+1=2? So yes!',
    'Even 0^2 = 1. I think you know what I\'m saying here...','Is 2+2 = 5? NO!',
    'I can\'t answer that.','HAHAHAHA... No.', "Silly question. But the answer is yes.",
    'Silly how the answer is no.', 'I\'m sure it\'s no... I think... Wait it\'s yes.',
    "I'm sure that i don't know.", "The latest study shows that the answer to your question is No.",
    "By carefuly examening your problem I have come to conclusion, that I don't know.",
    "Schrodinger's cat says it all.", "Anything but that question! Please have mercy on me.",
    "What are the odds of it being yes?","Doubtfull.","I think I agree.", "Without a doubt.", 
    "There are no questions about it.", "BITCH IT MIGHT BE!", 
    "If most people asked ask me I'd say no, but since you're asking it's yes.",
    "God himself is in doubt of it.", "Lucifer sayes yes.", 
    "Your guardian angel says No.", "No! Ow god no! NOOOO!", 
    "HELL YEA!!!!!", "My ex used to say yes to that", "( ͡° ͜ʖ ͡°)",
    "I'm not Einstain so I can't answer to this question.",
    "That's what they scream in bed (ohh yea)",
    "20% yes and 80% no.", "As long as I stand it's yes!", "50-50 chance.",
    "Here. I wrote you a poem:\n Roses are red,\n Violets are violet,\n I'm no Shakespear,\nand the answer is NO.\n\n P.S. I know my poem sucks.",
    "It's not no, if that's what you thought.", "It's not yes, if that's what you thought.",
    "Your answer is hidden in another castle.",
    "404 your answer is not found.", "Did you drink coffe today?", 
    "Ask your crush out. Teir answer is answer to this...", 
    "It can be whatever you want.", 
    "If you belive hard enaugh. But you have to belive hard enaugh!", 
    "There is somebody who can answer it, but it defineatly isn't me.",
    "Did you know jelly fish aren't actualy fish. On the other note I can't answer you.",
    "Let me role a dice...\n Hmmm this is strange...\n How can a 6 sided dice say Yes? \n Well yes it is then!",
    "This is an aincent message that been passed thru generations. Are you ready? It's no!",
    "I can't tell you, it would cause a space and time paradox.", "True", "False","????",
    "@£#&@£&@£#&@#%€", "Use your imagination ;)",
    "So I would answer it for you, but there are some questions you have to find answers by yourself.",
    "How dare you ask me such question? Do you have me for a fool???", "Be reasonable, we both know it's yes.",
    "Be reasonable, we both know it's no.", "<Write answer here>","There should be an answer here.",
    "Did you think I had the answer? Well you were wrong.", "God I wish I knew the answer to that question",
    "There is time and place for everything, even for this answer... It just isn't now.",
    "Well...I don't know what to say...I think you'll have to ask me some other time... Nah, I'm just shittomg with you, It's yes",
    "There is no easy way of saying this, but I gotta tell you it's no.", "Sometimes it's just ment to be no.",
    "Sometimes it's just ment to be no.Luckily this isn't one of those times, so it's yes.", 
    "If I had to guess, I'd say it's probable.","I rather not say, because I'm not sure.",
    "If I knew the answer to that question I wouldn't be here.", "HAIL NO!","HELL, why should I know?",
    "I miss 10s ago before I read this.", "Do you really want me to answer to that?",
    "I tryed my best but I can think only so much. In the end I came to conclusion it's yes.",
    "I tryed my best but I can think only so much. In the end I came to conclusion it's no.",
    "Fuck do I know?","Pfft...You wish!", "I just don't want to break your feelings.", 
    "Hope you can forgive me for being quiet...", 'Its yes and its no.',    
    'I refuse to cooperate.',"I won't be harassed, bitch!", 'I have the right to be silent!','Its my choice to say YES.','Unable to could.','0','1','True','False','42',"Are you white? If you are then it's yes, otherwise no.",
    "As long as I’m alive.","Just be sure that we won’t get caught.","Life’s too short to be saying no.","Who put you up to this? Tell me!","Kiss my butt first.","Have you forgotten? I’m a yes-man!","Thought you’d never ask!","Hell, you bet-cha, matey!","Even my dog is saying yes.","Let’s say I agreed to this. But, can I still change my mind later?","My answer would probably be yes, but I totally forgot—I have another appointment!","You should know my answer by the way I’m nodding my head up and down.","Just be sure that we won’t go to jail for this.","If I say yes, will you give me a million bucks?","Abso-f*kin-lutely!","Probably yes, but I’ll have my people call your people to discuss.","Even if I hate you, I would say yes to this one.","Say no more!","It would take a whole army to keep me from saying yes.","Right on the money!","Yes, yes, and yes!","You get my vote.","I love you, so yeah.","Give me a ‘Y.’ Give me an ‘E.’ Give me an ‘S.’ Give me a ‘Y-E-S!’","A thousand times, yes!","A million times, yes!","Aye, sir!","I would like to express my full approval.","Damn straight.","Goddamn right!","I agree to the fullest!","I agree.","True enough!","That is true.","I can’t argue with that!","We share the same sentiments.","That would be a Y-E-S!","Definitely not NO.","Hahaha, that’s true.","I do not disagree.","My answer is in the affirmative.","What’s the opposite of no?","If I was a regular jerk, I’d say no to this one.","Is the mitochondria the powerhouse of the cell?","Is the sun hot?","Do fishes swim?","Do pigeons fly?","Is the pope catholic?","Do vacuum cleaners suck?","Is water wet?","Is the hypotenuse the longest side of a triangle?","Does a bear live in the woods?","I’ll answer you with my favorite ‘Y’ word—Yes!","Is the sky blue?","How do you spell yes?","Would you take ‘yes’ for an answer?","There’s a 100% chance that I’m going say yes to that one.","Oh yeah, baby!","There is a huge possibility that you are correct.","I’m leaning towards yes, but what’s in it for me?","Upon close examination of the aforementioned data, I wholeheartedly accept your conclusion as plausible.","You are going to regret asking me this.","You’ve gotta be kidding me!","The answer is a resounding yes!",
    "Would love to say yes, but my dog told me to say no.","Sorry, I can’t say yes. I have to walk my unicorn.","My advisors have come to a unanimous decision, and it’s a—NO!","The voices in my head are asking me to say ‘no’ to this one.","That’s such a funny joke! HAHAHAHA!","It’s N to the O!","I would say no even if you kiss my butt.","You know what season it is? It’s the season of NO!","That sounds like effort, so no.","Does it involve me moving from where I am right now? If the answer is yes, then I would have to say no.","I would love to say yes, but I actually wouldn’t love to say yes.","Give me an ‘N.’ Give me an ‘O.’ Give me an ‘N-O!’","Not today, Satan! Not today.","Please email your concern to ‘idontcare.com’ and I’ll send you my decision in a hundred years.","I would love to say yes, but unfortunately...no.","Negative!","My answer is a resounding no!","There’s a hundred percent chance that I’m going to say ‘no’ to this one.","No means no, now let it go.","I think not.","Frankly, my dear—no!","You should rethink your idea.","There are worse things I could say ‘yes’ to. I just can’t think of any at the moment.","Why, heavens no!","Oh, hell no!","I have a bad feeling about this, so no.","My parents said no.","No no no no no no no no no no no!","On a scale of maybe to absolutely, I would say—absolutely not!","In another life, perhaps?","What part of the word ‘no’ do you not understand?","My future self says no!","I would only say ‘yes’ if hell has already frozen over.","It’s that time of the year when I usually always say no.","Regrettably, I’m a no-man!","Liar, liar, panties on fire!","I’m going to have to flex my ‘no’ muscle on this one.","Shop is closed! Come back again tomorrow.","Sorry, no answer here, better luck next time.","Saying ‘yes’ would surely cause the slow, withering death of soul.","What’s the opposite of yes?","Is a dog a human?","How do you spell no?","Do fishes fly?","Ask me again in a few years.","How does ‘no’ sound to you?","I’m way too smart to say ‘yes’ to that.","What’s the opposite of positive?","Is the sky green?","Is water dry?","Give a moment. I’m trying to see how long I can go without saying yes.","How does ‘never’ work for you?","Is the sun cold?","Would you take ‘no’ for an answer?","Over my dead body!","Ewwww...no!","You do know I hate you, right?","Not in a hundred years!","Not in a million years!","Not in a billion years!","Let’s just pretend that we don’t know each other.","Which of the following is the funniest way to say 'no' for you?","That question is bad, and you should be punished!","Umm...no!",'I have decided that I don\'t know and I don\'t care.'
    ]
def _8ball():
    return(outputs[randint(0,len(outputs)-1)])


def all_8ball():
    return(outputs)
