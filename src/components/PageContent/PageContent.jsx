import React from 'react';
import s from './PageContent.module.css';
import { Routes, Route } from 'react-router-dom';
import SearchSong from '../SearchPanel/SearchSong';
import SearchGroup from '../SearchPanel/SearchGroup';
import SearchPanel from '../SearchPanel/SearchPanel';

const PageContent = () => {
    return (
        <div className={s.page__wrapper}>

            <Routes>
                <Route path='/' element={<SearchPanel />} />
                <Route path='/search-for-group' element={<SearchGroup />} />
                <Route path='/search-for-song' element={<SearchSong />} />
            </Routes>
        </div>
    )
}

export default PageContent;