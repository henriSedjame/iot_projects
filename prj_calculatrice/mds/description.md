# 🧮 LA CALCULATRICE

<p class="description"> 
Ce projet de <strong>calculatrice</strong> vise à créer une calculatrice qui permettra de réaliser des opérations mathématiques de base.
</p>

<h4 style="padding-left: 50px;">
<span style="font-size: 1.5em; margin-right: 5px">🤨</span>   Une vraie calculatrice ❓ ❓
</h4>

<p style="padding-left: 50px;"> 
<span style="font-size: 1.5em; margin-right: 5px"> 😉</span>  Eh oui, une vraie de vrai
</p>

<h4 style="padding-left: 50px;">
<span style="font-size: 1.5em; margin-right: 5px">🤔</span> Et comment on fait ça ?
</h4>

<p style="padding-left: 50px;"> 
Je vais t'expliquer !!
<p style="padding-left: 50px;"> 
    D'abord, on a besoin de quelques composants pour créer notre calculatrice :
</p>
<br/><br/>

<ul>

<li class="component"> <strong style="text-transform: uppercase; font-size: .75em"> Un clavier matriciel</strong> <br/><br/>
<div class="description-component">
<img src="../../assets/keypad.jpeg" width=150 alt="keypad"><br>

        Le clavier matriciel est un type de clavier dont la disposition s'apparente à une matrice et qui est utilisé comme périphérique pour les microcontrôleurs
</div>

C'est le clavier de notre calculatrice. 

Il permettra à l'utilisateur de saisir les nombres et les opérations à effectuer.

</li><br/>

<li class="component"> <strong style="text-transform: uppercase; ; font-size: .75em">Un écran lcd i2c</strong> <br/>
<div class="description-component">
<img src="../../assets/lcd.jpg" width=150 alt="ecran lcd"><br> 


</div>

Et là c'est l'écran qui affichera la saisie de l'utilisateur et le résultat des opérations effectuées.

</li><br/>

<li class="component"> <strong style="text-transform: uppercase; ; font-size: .75em">micro-contrôleur </strong> <br/>
<div class="description-component">
<img src="../../assets/rpi.jpeg" width=150 alt="Moteur servo"><br> 

        Un microcontrôleur est un circuit intégré qui rassemble les éléments essentiels d'un ordinateur.
</div>
<div class="rpi-content">
<div>
En fait, un microcontrôleur, c'est comme un tout petit ordinateur 🖥️.

Celui là s'appelle <span class="rpi"> <img src="../../assets/rpi-logo.png" width=15 alt="Raspberry Pi Pico">  Raspberry Pi Pico</span>

Il sera le 🧠 cerveau de notre poubelle.

🤔...

<span class="dialog-bulle">Okay 🙄 bon, il faudra quand même lui dire exactement ce qu'on attend de lui...</span>

🤔...

<span class="dialog-bulle"> Il faudra le lui dire dans un langage qu'il comprend 🤗 ... <strong>le python 🐍</strong> </span>

😱...

<span class="dialog-bulle">🤣 Non, python, c'est un langage informatique ☺️</span>
</div>

</div>
</li><br/>

</ul>
</p>

<p style="padding-left: 50px;">
Eh oui !!! Nous allons écrire un <strong>programme informatique</strong> en <strong> language python 🐍</strong> pour piloter notre calculatrice. 
</p>

<p style="padding-left: 50px;">
C'est ce qu'on appelle un <strong>système embarqué</strong>
</p>

<h3 style="padding-left: 50px; padding-top: 20px; padding-bottom: 10px;">
SCHEMA DE NOTRE CIRCUIT
</h3>

<p style="padding-left: 50px;">
Voilà un peu à quoi devra ressembler notre circuit.
</p>

<p style="padding-left: 50px;">
Nous aurons besoin de quelques cables 🧶pour relier nos composants entre eux.
</p>

<p style="padding-left: 50px;">
⚠️ Prenez soin de choisir des cables de la bonne couleur pour ne pas vous perdre dans vos branchements️ 😜
</p>
<div style="padding-left: 50px;">
<img src="../../assets/calc_schema.png" width=800 alt="schema">
</div>


<p style="padding-left: 50px; font-size: 1.2em;">
Allez au travail 😜!!! 
</p><br>

<p style="padding-left: 50px; font-style: italic;">
Je vous mets le code final 👇 ici. Vous pourrez le consulter après les explications.
</p>




