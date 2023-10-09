import React from 'react';
import s from './MainContent.module.css';
import SongCard from '../Cards/SongCard/SongCard';

const MainContent = (props) => {
    let songs = props.data.map(el => 
        <SongCard 
            albumName = {el.album} 
            groupName = {el.group}
            groupDescription = 'Sabaton - swedish heavy metal band that was started in Falun.' 
            groupCover = ''  
            songTitle = {el.title} 
            whenAdded = {el.time_create} 
        />)

    return (
        <main className={s.main_page}>
            <span className={s.main_page__title}>Recently added:</span>
            <div className={s.main_page__wrapper}>
                {songs}
            </div>
        </main>
    )
}

export default MainContent;

