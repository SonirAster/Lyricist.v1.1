import React, { useEffect, useState } from 'react';
import axios from 'axios';
import s from './PageContent.module.css';
import { Routes, Route } from 'react-router-dom';
import MainContent from '../MainContent/MainContent';
import SearchSong from '../SearchSong/SearchSong';
import SearchGroup from '../SearchGroup/SearchGroup';
import SearchPanel from '../SearchPanel/SearchPanel';

const PageContent = () => {
    let src='http://localhost:8000' 
    const [data, setData] = useState([]);
    useEffect(() => {
        axios
        .get(src)
        .then(res => {
            setData(res.data);
        })
    }, []);

    return (
        <div className={s.page__wrapper}>
            <SearchPanel />
            <Routes>
                <Route path='/' element={<MainContent data={data} />} />
                <Route path='/group' element={<SearchGroup />} />
                <Route path='/song' element={<SearchSong />} />
            </Routes>
        </div>
    )
}

export default PageContent;

