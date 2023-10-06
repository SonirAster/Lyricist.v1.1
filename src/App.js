import React from 'react';
import './App.css';
import Header from './components/Header/Header';
import PageContent from './components/PageContent/PageContent';
import Footer from './components/Footer/Footer';

 const App = () => {
    return (
        <div className='app-wrapper'>
            <Header />
            <PageContent />
            <Footer />
        </div>
    )
}
    
export default App;

