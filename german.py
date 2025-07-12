import streamlit as st

st.set_page_config(page_title="German B1 Grammar Guide", layout="wide")

st.title("🇩🇪 German B1 Grammar Guide & Practice")
st.markdown("""
Welcome! This interactive guide is designed for learners preparing for the **B1 German exam**.
Explore each grammar topic with explanations, tables, lots of examples, and short practice exercises.
""")

topics = [
    "Tenses",
    "Modal Verbs",
    "Passive Voice",
    "Subordinate Clauses",
    "Relative Clauses",
    "Konjunktiv II",
    "Adjective Endings",
    "Pronouns",
    "Prepositions",
    "Noun Declension",
    "Verbs with Prepositions",
    "Word Order",
    "Comparative & Superlative",
    "Negation",
    "Vocabulary Themes"
]
tabs = st.tabs(topics)

# --- Tenses ---
with tabs[0]:
    st.header("1. Tenses (Zeitformen)")
    st.markdown("""
    ### Präsens (Present Simple)
    - Ich lerne Deutsch. _(I am learning German.)_
    - Wir wohnen in Berlin. _(We live in Berlin.)_

    ### Perfekt (Present Perfect)
    - Ich habe Deutsch gelernt. _(I have learned German.)_
    - Wir sind nach Berlin gefahren. _(We have gone to Berlin.)_

    **Note:** Use "haben" for most verbs, "sein" for verbs showing movement or change.
    """)
    st.markdown("""
    ### Präteritum (Simple Past)
    - Ich ging nach Hause. _(I went home.)_
    - Es regnete den ganzen Tag. _(It rained all day.)_

    ### Futur I (Future Simple)
    - Ich werde Deutsch lernen. _(I will learn German.)_
    """)
    st.subheader("Practice")
    q = st.radio("How do you say 'I have eaten' in German?",
                 ["Ich esse.", "Ich habe gegessen.", "Ich werde essen."])
    if q == "Ich habe gegessen.":
        st.success("Correct!")
    else:
        st.error("Not quite. Try again!")

# --- Modal Verbs ---
with tabs[1]:
    st.header("2. Modal Verbs (Modalverben)")
    st.markdown("""
    Six modal verbs:
    - dürfen (may, be allowed to)
    - können (can, be able to)
    - mögen (like)
    - müssen (must, have to)
    - sollen (should)
    - wollen (want)

    **Present:**  
    - Ich kann schwimmen. _(I can swim.)_
    - Darf ich gehen? _(May I go?)_

    **Simple Past:**  
    - Er musste arbeiten. _(He had to work.)_

    **Perfekt (double infinitive):**  
    - Ich habe gehen müssen. _(I had to go.)_
    """)
    st.subheader("Practice")
    q = st.radio("Which is correct for 'I had to work'?",
                 ["Ich habe arbeiten müssen.", "Ich habe gemusst arbeiten.", "Ich arbeitete müssen."])
    if q == "Ich habe arbeiten müssen.":
        st.success("Correct!")
    else:
        st.error("Try again!")

# --- Passive Voice ---
with tabs[2]:
    st.header("3. Passive Voice (Passiv)")
    st.markdown("""
    **Present Passive:**  
    - Das Haus wird gebaut. _(The house is being built.)_

    **Past Passive:**  
    - Das Haus wurde gebaut. _(The house was built.)_

    **Man-Form:**  
    - Man baut das Haus. _(The house is being built.)_
    """)
    st.subheader("Practice")
    q = st.radio("Translate: 'The letter is being written.'",
                 ["Der Brief wird geschrieben.", "Der Brief ist geschrieben.", "Der Brief schreibt."])
    if q == "Der Brief wird geschrieben.":
        st.success("Correct!")
    else:
        st.error("Not quite!")

# --- Subordinate Clauses ---
with tabs[3]:
    st.header("4. Subordinate Clauses (Nebensätze)")
    st.markdown("""
    Words: **weil**, **dass**, **wenn**, **obwohl**, **während**, **nachdem**, **bevor**, **als**, **ob**

    **Rule:** Verb goes to the end in the subordinate clause.

    - Ich lerne Deutsch, weil ich in Deutschland arbeiten möchte.  
      _(I learn German because I want to work in Germany.)_
    - Sie sagt, dass sie morgen kommt. _(She says that she is coming tomorrow.)_

    **Indirect questions:**  
    - Können Sie mir sagen, wo der Bahnhof ist? _(Can you tell me where the station is?)_
    """)
    st.subheader("Practice")
    q = st.radio("Which is correct?",
                 ["Ich gehe ins Kino, weil ich habe Zeit.", "Ich gehe ins Kino, weil ich Zeit habe."])
    if q == "Ich gehe ins Kino, weil ich Zeit habe.":
        st.success("Correct!")
    else:
        st.error("Nope! Remember the verb goes to the end.")

# --- Relative Clauses ---
with tabs[4]:
    st.header("5. Relative Clauses (Relativsätze)")
    st.markdown("""
    Use: **der, die, das, deren, dessen, denen**  
    Relative clause describes a noun and the verb goes to the end.

    - Das ist der Mann, **der** hier wohnt. _(That is the man who lives here.)_
    - Das ist die Frau, **deren** Auto rot ist. _(That's the woman whose car is red.)_

    **With prepositions:**  
    - Das Buch, **in dem** ich lese, ist spannend. _(The book in which I am reading is exciting.)_
    """)
    st.subheader("Practice")
    q = st.radio("Choose the correct relative pronoun: 'Das ist die Frau, ___ Auto rot ist.'",
                 ["deren", "dessen", "deren's"])
    if q == "deren":
        st.success("Correct!")
    else:
        st.error("Careful, 'deren' is used for feminine/ plural whose.")

# --- Konjunktiv II ---
with tabs[5]:
    st.header("6. Konjunktiv II (Subjunctive)")
    st.markdown("""
    Used for politeness, wishes, unreal situations.

    - **Polite:** Könnten Sie mir helfen? _(Could you help me?)_
    - **Wishes:** Wenn ich mehr Zeit hätte... _(If I had more time...)_
    - **Hypothetical:** Wenn ich reich wäre, würde ich reisen. _(If I were rich, I would travel.)_
    """)
    st.subheader("Practice")
    q = st.radio("How to say 'If I had money, I would buy a car.'?",
                 ["Wenn ich Geld hätte, würde ich ein Auto kaufen.",
                  "Wenn ich Geld habe, würde ich ein Auto kaufen.",
                  "Wenn ich Geld hätte, kaufe ich ein Auto."])
    if q == "Wenn ich Geld hätte, würde ich ein Auto kaufen.":
        st.success("Correct!")
    else:
        st.error("Try again! Remember 'hätte ... würde' for unreal.")

# --- Adjective Endings ---
with tabs[6]:
    st.header("7. Adjective Endings (Adjektivendungen)")
    st.markdown("""
    **Depends on:** Article (definite/indefinite/none) and Case (Nominative, Accusative, Dative, Genitive).

    - Der _gute_ Mann (Nom, definite)
    - Ein _guter_ Mann (Nom, indefinite)
    - Ich sehe einen _guten_ Mann (Akk, indefinite)
    - Mit einem _guten_ Mann (Dat, indefinite)
    """)
    st.markdown("""
    | Case / Article      | Masculine        | Feminine         | Neuter           | Plural          |
    |---------------------|------------------|------------------|------------------|-----------------|
    | der (Nom)           | der gute Mann    | die gute Frau    | das gute Kind    | die guten Leute |
    | ein (Akk)           | einen guten Mann | eine gute Frau   | ein gutes Kind   | --              |
    """)
    st.subheader("Practice")
    q = st.radio("Fill the blank: Ich sehe ___ schönen Hund.",
                 ["den", "dem", "der"])
    if q == "den":
        st.success("Correct! (Akkusativ, der Hund)")
    else:
        st.error("Think: Akkusativ of 'der'.")

# --- Pronouns ---
with tabs[7]:
    st.header("8. Pronouns (Pronomen)")
    st.markdown("""
    - **Personal:** ich, du, er, sie, es, wir, ihr, sie, Sie
    - **Reflexive:** sich waschen (to wash oneself)
    - **Possessive:** mein, dein, sein, ihr, unser, euer, ihr, Ihr
    - **Demonstrative:** dieser, jener, derjenige, derselbe
    - **Relative:** der, die, das, deren, dessen, denen
    - **Indefinite:** jemand, niemand, etwas, nichts, man, alle, einige, viele
    """)
    st.subheader("Practice")
    q = st.radio("Which is reflexive? (I wash myself)",
                 ["Ich wasche mich.", "Ich wasche den Hund.", "Ich mich wasche."])
    if q == "Ich wasche mich.":
        st.success("Exactly!")
    else:
        st.error("Check for reflexive pronoun.")

# --- Prepositions ---
with tabs[8]:
    st.header("9. Prepositions (Präpositionen)")
    st.markdown("""
    - **Accusative:** durch, für, gegen, ohne, um
    - **Dative:** aus, bei, mit, nach, seit, von, zu
    - **Genitive:** während, wegen, trotz, statt, außerhalb
    - **Two-way (Wechsel):** an, auf, hinter, in, neben, über, unter, vor, zwischen

    **Examples:**
    - Ich gehe **in** die Schule. _(Akk, movement)_
    - Ich bin **in** der Schule. _(Dat, location)_
    """)
    st.subheader("Practice")
    q = st.radio("Choose the correct case: 'Ich gehe in ___ Park.'",
                 ["den", "dem", "der"])
    if q == "den":
        st.success("Correct! (Akkusativ, movement)")
    else:
        st.error("Remember: movement = Akkusativ.")

# --- Noun Declension ---
with tabs[9]:
    st.header("10. Noun Declension (Deklination)")
    st.markdown("""
    **Cases:** Nominative, Accusative, Dative, Genitive

    - der Hund, den Hund, dem Hund, des Hundes
    - die Frau, die Frau, der Frau, der Frau
    - das Buch, das Buch, dem Buch, des Buches

    **Plural:**  
    - die Hunde, die Frauen, die Bücher
    """)
    st.subheader("Practice")
    q = st.radio("What is the Genitive of 'das Kind'?",
                 ["des Kindes", "dem Kind", "der Kind"])
    if q == "des Kindes":
        st.success("Right!")
    else:
        st.error("Check Genitive endings for neuter.")

# --- Verbs with Prepositions ---
with tabs[10]:
    st.header("11. Verbs with Prepositions")
    st.markdown("""
    - **warten auf** (to wait for): Ich warte **auf** den Bus.
    - **denken an** (to think of/about): Ich denke **an** dich.
    - **sich freuen über/auf**: Ich freue mich **auf** das Wochenende.
    - **sprechen mit/über**: Wir sprechen **über** das Problem.
    """)
    st.subheader("Practice")
    q = st.radio("Which is correct?",
                 ["Ich warte auf dich.", "Ich warte dich.", "Ich dich warte auf."])
    if q == "Ich warte auf dich.":
        st.success("Correct!")
    else:
        st.error("Watch the preposition!")

# --- Word Order ---
with tabs[11]:
    st.header("12. Word Order (Wortstellung)")
    st.markdown("""
    - **Main clause:** Verb is in 2nd position:  
      Ich **gehe** morgen ins Kino.
    - **Subordinate clause:** Verb at the end:  
      ...weil ich morgen ins Kino **gehe**.
    - **Questions:** Verb first (W-questions, yes/no):  
      Gehst du ins Kino?  
      Wann gehst du ins Kino?
    - **Imperative:**  
      Geh ins Kino!
    - **Time-Manner-Place (TMP):**  
      Ich gehe **am Samstag** (Time) **mit meinen Freunden** (Manner) **ins Kino** (Place).
    """)
    st.subheader("Practice")
    q = st.radio("What is the correct word order?",
                 ["Ich fahre morgen mit dem Bus zur Arbeit.",
                  "Ich morgen mit dem Bus zur Arbeit fahre.",
                  "Morgen ich fahre mit dem Bus zur Arbeit."])
    if q == "Ich fahre morgen mit dem Bus zur Arbeit.":
        st.success("Yes! TMP and verb 2nd.")
    else:
        st.error("Review TMP and verb position.")

# --- Comparative & Superlative ---
with tabs[12]:
    st.header("13. Comparative & Superlative")
    st.markdown("""
    - **Comparative:** größer (bigger), schöner (prettier)
    - **Superlative:** am größten (biggest), am schönsten (prettiest)
    - **Irregulars:** gut → besser → am besten; viel → mehr → am meisten
    - **als** (than), **wie** (as)

    **Examples:**
    - Mein Haus ist größer **als** dein Haus.  
      _(My house is bigger than your house.)_
    - Ich bin so groß **wie** du.  
      _(I am as tall as you.)_
    """)
    st.subheader("Practice")
    q = st.radio("How do you say 'He is the best'?",
                 ["Er ist am besten.", "Er ist besser.", "Er ist der best."])
    if q == "Er ist am besten.":
        st.success("Great job!")
    else:
        st.error("Superlative uses 'am' and '-sten'.")

# --- Negation ---
with tabs[13]:
    st.header("14. Negation (Negation)")
    st.markdown("""
    - **nicht**: negates verbs, adjectives, adverbs, or whole sentences.
    - **kein**: negates nouns (no, none).
    - **Double negation:** Rare in German (often incorrect).

    **Examples:**
    - Ich habe **kein** Geld. _(I have no money.)_
    - Ich gehe **nicht** ins Kino. _(I am not going to the cinema.)_
    """)
    st.subheader("Practice")
    q = st.radio("Which is correct?",
                 ["Ich habe keinen Hund.", "Ich habe nicht Hund.", "Ich habe Hund nicht."])
    if q == "Ich habe keinen Hund.":
        st.success("Nice!")
    else:
        st.error("Use 'kein' for nouns.")

# --- Vocabulary Themes ---
with tabs[14]:
    st.header("15. Vocabulary Themes (Wortschatz)")
    st.markdown("""
    **Everyday life:** Familie, Arbeit, Reisen, Gesundheit, Einkaufen, Medien, Kultur  
    **Abstract topics:** Meinungen, Argumente, Wünsche, Pläne, Gefühle, Probleme

    _Some examples:_
    - Familie: Mutter, Vater, Geschwister, Onkel, Tante
    - Arbeit: Kollege, Chef, Firma, Gehalt, Bewerbung
    - Reisen: Urlaub, Flug, Bahn, Hotel, buchen
    - Gesundheit: Arzt, Krankheit, gesund, Tablette, Rezept
    - Einkaufen: Supermarkt, Angebot, bezahlen, billig, teuer
    - Medien: Zeitung, Fernsehen, Nachricht, Internet, senden
    """)
    st.subheader("Practice")
    q = st.radio("What is 'health' in German?",
                 ["Arbeit", "Gesundheit", "Kultur"])
    if q == "Gesundheit":
        st.success("Richtig! 🎉")
    else:
        st.error("Try again!")

st.info("Tip: Review and practice regularly. Viel Erfolg beim Deutschlernen! 🇩🇪")

