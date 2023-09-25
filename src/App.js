import React from 'react';
import './App.css';
import Header from './components/Header/Header';
import PageContent from './components/PageContent/PageContent';
import Footer from './components/Footer/Footer';

// class App extends React.Component {
//     state = { details: [], }
//     componentDidMount(){
//         let data;
//         axios.get('http://localhost:8000/group')
//         .then(res => {
//             data = res.data;
//             this.setState({
//                 details: data
//             });
//             console.log(data);
//         })
//         .catch(err => {
//             console.log(err);
//         })

//     }
//     render() {
//         return (
//             <div className='app-wrapper'>
//                 <Header />
//                 <PageContent />
//             </div>
//         )
//     }
// }

// let [state, setState] = useState({ details: [], });
// setState({
//     details: data
// });

// const App = (props) => {
//     // let data;
//     axios.get('http://localhost:8000/group')
//     .then(res => {
//        GetData(res.data)
//         console.log(GetData);
//     })

//     return (
//         <div className='app-wrapper'>
//             <Header />
//             <PageContent />
           
//         </div>
//     )
// }

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

