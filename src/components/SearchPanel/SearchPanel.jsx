import React from 'react';
import s from './SearchPanel.module.css';
import { NavLink } from 'react-router-dom';
import panel from './panel.jpg';

const SearchPanel = () => {
    return (
        <div className={s.search_panel}>
            <div className={s.search_group}>
                <div className={s.search_group__image}><img src={panel}/></div>
                <NavLink to="/search-for-group" className={s.search_group__title}>Seek for Group</NavLink>
            </div>
            <div className={s.search_song}>
                <NavLink to="/search-for-song">Seek for Song</NavLink>
            </div>
        </div>
    )
}

export default SearchPanel;
