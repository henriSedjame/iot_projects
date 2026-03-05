# 🌱 L'ARROSOIR AUTOMATIQUE
 
<p class="description"> 
L' <strong>arrosoir automatique</strong> est un arrosoir qui décide par lui même d'arroser la plante quand il estime que cette dernière n'a plus assez d'eau.
</p>

<h4 style="padding-left: 50px;">
<span style="font-size: 1.5em; margin-right: 5px">😍</span>   Waouh, mais c'est génial ‼️
</h4>

<p style="padding-left: 50px;"> 
<span style="font-size: 1.5em; margin-right: 5px"> 😉</span>  Eh oui, comme tu dis, c'est <strong>GE-NIAL</strong>
</p>

<h4 style="padding-left: 50px;">
<span style="font-size: 1.5em; margin-right: 5px">🤔</span> Mais attend, comment un arrosoir pourrait arroser tout seul ? Et surtout comment un arrosoir pourrait savoir quand il faut arroser ?
</h4>

<p style="padding-left: 50px;"> 
C'est ce que nous allons essayer de comprendre et surtout de réaliser 🥸.
</p>
<p style="padding-left: 50px;"> 
D'abord, pour qu'un arrosoir puisse devenir autonome, il faut le doter de quelques composants :
</p>

<ul>

<li class="component"> <strong style="text-transform: uppercase; font-size: .75em"> un capteur d'humidité du sol</strong> <br/><br/>
<div class="description-component">
<img src="../../assets/capteur_humidite.jpg" width=150 alt="Capteur ultrason"><br>

        Les capteurs d'humidité du sol mesurent la teneur en eau volumétrique du sol
</div>

Voilà le premier allié de notre arrosoir. 

C'est lui qui sera chargé de dire la quantité d'eau qu'on a dans la terre 🪴.

</li><br/>

<li class="component"> <strong style="text-transform: uppercase; ; font-size: .75em">une mini pompe à moteur submersible</strong> <br/><br>
<div class="description-component">
<img src="../../assets/pump.jpg" width=150 alt="Moteur servo"><br> 
        
        Une pompe submersible (ou pompe électrique submersible (ESP)) est un dispositif qui possède un moteur 

        hermétiquement scellé étroitement couplé au corps de la pompe.

</div>

Lui 👆, c'est l'élément central de notre arrosoir.

Il peut, grâce à son moteur 📽️, pomper de l'eau 🌊 qui servira à arroser la plante 🌱.


⚠️ Mais, notre pompe aura besoin de deux autres aliés pour fonctionner correctement.

Il s'agit de : 
<ul>
<li> <strong style="text-transform: uppercase; ; font-size: .7em">la pile</strong> <br/><br>
<div class="description-component">
<img src="../../assets/pile.jpg" width=40 alt="Pile"><br>
             
     La pile servira de source d'énergie pour notre pompe.
        
</div>
</li><br>

<li> <strong style="text-transform: uppercase; ; font-size: .7em">du relay</strong> <br/><br>
        <div class="description-component">
        <img src="../../assets/relay.jpeg" width=100 alt="Pile"><br>
             
     Le relay sera utilisé pour 

        1/ connecter la pompe à la pile

        2/ contrôler l'alimentation de la pompe d'autre part
    
    Eh oui on doit pouvoir allumer et arrêter la pompe au besoin 😉!!!
        
</div>
</li>
</ul>

</li><br/>

<li class="component"> <strong style="text-transform: uppercase; ; font-size: .75em">un micro-contrôleur </strong> <br/>
<div class="description-component">
<img src="../../assets/rpi.jpeg" width=150 alt="Moteur servo"><br> 

        Un microcontrôleur est un circuit intégré qui rassemble les éléments essentiels d'un ordinateur.
</div>
<div class="rpi-content">
<div>
En fait, un microcontrôleur c'est comme un tout petit ordinateur 🖥️.

Celui là s'appelle <span class="rpi"> <img src="../../assets/rpi-logo.png" width=15 alt="Raspberry Pi Pico">  Raspberry Pi Pico</span>

Il sera le 🧠 cerveau de notre arrosoir.

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
Eh oui !!! Nous allons écrire un <strong>programme informatique</strong> en <strong> language python 🐍</strong> pour piloter notre arrosoir. 
</p>

<p style="padding-left: 50px;">
C'est ce qu'on appelle un <strong>système embarqué</strong>
</p>


<h3 style="padding-left: 50px; padding-top: 20px; padding-bottom: 10px; color: #011451;">
🔌 SCHEMA DE NOTRE CIRCUIT
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
<img src="../../assets/arr_schema.png" width=800 alt="schema">
</div>


<h3 style="padding-left: 50px; padding-top: 20px; padding-bottom: 10px; color: #011451;">
💻 CODE
</h3>

<p style="padding-left: 50px; ">
👍 Une fois tout bien cablé, il est temps de programmer la logique 🎲 de notre arrosoir .
</p>

<p style="padding-left: 50px; font-style: italic;">
Je vous mets le code final 👇 ici. Vous pourrez le consulter après les explications.
</p>



