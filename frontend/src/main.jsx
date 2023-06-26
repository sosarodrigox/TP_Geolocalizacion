import React from 'react'
import ReactDOM from 'react-dom/client'
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import Home from './componentes/home'
import Datos from './componentes/datos'
import Consultas from './componentes/consultas'
import PaisesLista from './componentes/paises/paises-lista'
import 'bootstrap/dist/css/bootstrap.min.css'

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />}>
          <Route path="datos" element={<Datos />}>
            <Route path='paises' element={<PaisesLista />}></Route>
          </Route>
          <Route path='consultas' element={<Consultas />}>

          </Route>
        </Route>
      </Routes>
    </BrowserRouter>
  </React.StrictMode>
)
