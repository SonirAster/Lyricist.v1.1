import React from 'react';
import s from './GroupCard.module.css';
import pickRandomCover from '../getCardCover';

const GroupCard = () => {
    let groupName = 'Sabaton';
    let groupCover = '#';
    let groupDescription = 'Sabaton - swedish heavy metal band that was started in Falun.';
    let groupYear = '1998';
    return (
        <div className={s.card}>
            <div className={s.card__cover}>
                <img src={pickRandomCover()} alt="cover" />
            </div>
            <main className={s.card_wrapper}>
                <section className={s.card__title}>
                    <a href="#">{groupName}</a>
                </section>
                <section className={s.card__group_image}>
                    <img src={groupCover} alt="image" />
                </section>
                <section className={s.card__group_desc}>
                    {groupDescription}
                </section>
                <section className={s.card__group_languages}>
                    <span>Sings in:</span>
                    <ul className={s.card__group_languages_list}>
                        <li className={s.card__group_list__language}>English</li>
                        <li className={s.card__group_list__language}>Swedish</li>
                    </ul>
                </section>
                <section className={s.card__when}>
                    Started in: <span>{groupYear}</span>
                </section>
            </main>
        </div>
    )
}

export default GroupCard;
