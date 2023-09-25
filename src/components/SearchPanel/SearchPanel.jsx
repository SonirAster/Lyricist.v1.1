import React from 'react';
import s from './SearchPanel.module.css';
import { NavLink } from 'react-router-dom';
import panel1 from './search1.jpg';
import panel2 from './search2.jpg';

const SearchPanel = () => {
    return (
        <div className={s.search_panel}>
            <div className={s.search_group}>
                <div className={s.search_group__image}><img src={panel1}/></div>
                <NavLink to="/group" className={s.search_group__title}>Seek for Group</NavLink>
            </div>
            <div className={s.search_song}>
                <div className={s.search_song__image}><img src={panel2}/></div>
                <NavLink to="/song" className={s.search_song__title}>Seek for Song</NavLink>
            </div>
        </div>
    )
}

export default SearchPanel;
