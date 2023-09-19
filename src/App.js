import axios from 'axios';
import './App.css';
import React from 'react';
import Header from './components/Header/Header';
import PageContent from './components/PageContent/PageContent';

const App = () => {
    axios.get('http://localhost:8000').then(data => console.log(data));
        return (
            <div className='app-wrapper'>
                <Header />
                <PageContent />
            </div>
        )
    }
export default App;

