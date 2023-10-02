import React from 'react';
import s from './MainContent.module.css';
import SongCard from '../Cards/SongCard/SongCard';

const MainContent = () => {
    return (
        <main className={s.main_page}>
            <span className={s.main_page__title}>Recently added:</span>
            <div className={s.main_page__wrapper}>
                <SongCard />
                <SongCard />
                <SongCard />
                <SongCard />
                <SongCard />
                <SongCard />
                <SongCard />
            </div>
        </main>
    )
}

export default MainContent;


