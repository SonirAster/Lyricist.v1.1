import React from 'react';
import s from './SongCard.module.css';
import { useRef } from 'react';
import pickRandomCover from '../getCardCover';

let songName = 'Kingdom Come';
let albumName = 'Fist for Fight';
let groupName = 'Sabaton';
let cover = './d.jpg';
let groupDescription = 'Sabaton - swedish heavy metal band that was started in Falun.';
let whenAdded = '27.07.2022';

const SongCard = () => {

    const ref = useRef();
    if (groupDescription.length > 90) {
        ref.current.style.padding = '15px';
        ref.current.style.minWidth = '220px';
        ref.current.style.minHeight = '200px';
    } 

    return (
        <div className={s.card}>
            <div className={s.card__image}>
                <img src={pickRandomCover()} alt="cover" />
            </div>
            <div className={s.card_wrapper}>
                <section className={s.card__title}>
                    <a href="#">{songName}</a>
                </section>
                <section className={s.card__album}>
                    <span>Album: </span> <br />
                    <a href="#">{albumName}</a>
                </section>
                <section className={s.card__group}>
                    <span>Band:</span> <br />
                    <div className={s.card__group_title}>
                        <a href="#">{groupName}</a>
                        <div  ref={ref} className={s.card__group_desc}>
                            <div className={s.card__desc_text}>
                                <div className={s.card__group_desc__group_image}>
                                    <img src={cover} alt="image" />
                                </div>
                                {groupDescription}
                            </div>
                            <div className={s.card__group_cover}>
                                <img src={pickRandomCover()} alt="cover" />
                            </div>
                        </div>
                    </div>
                </section>
            </div>
            <div className={s.card__when}>
                Added: <span>{whenAdded}</span>
            </div>
        </div>
    )
}

export default SongCard;