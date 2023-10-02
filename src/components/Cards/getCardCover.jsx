import React from 'react';
import cover1 from './img/photo1.jpg';
import cover2 from './img/photo2.jpg';
import cover3 from './img/photo3.jpg';
import cover4 from './img/photo4.jpg';

let  cardCovers = [];
cardCovers.splice(0, 0, cover1, cover2, cover3, cover4);

const pickRandomCover = () => {
    return cardCovers[Math.floor(Math.random() * cardCovers.length)];
}

export default pickRandomCover;