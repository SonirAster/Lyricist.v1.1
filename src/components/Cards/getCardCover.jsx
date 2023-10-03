import React from 'react';
import cover1 from './img/photo1.jpg';
import cover2 from './img/photo2.jpg';
import cover3 from './img/photo3.jpg';
import cover4 from './img/photo4.jpg';
import cover5 from './img/photo5.jpg';
import cover6 from './img/photo6.jpg';
import cover7 from './img/photo7.jpg';
import cover8 from './img/photo8.jpg';
import cover9 from './img/photo9.jpg';

let  cardCovers = [];
cardCovers.splice(0, 0, cover1, cover2, cover3, cover4, cover5, cover6, cover7, cover8, cover9);

const pickRandomCover = () => {
    return cardCovers[Math.floor(Math.random() * cardCovers.length)];
}

export default pickRandomCover;