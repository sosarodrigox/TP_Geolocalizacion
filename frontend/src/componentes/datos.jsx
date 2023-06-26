import React from "react";
import { NavLink, Outlet } from "react-router-dom";

export default function Datos() {
    return (
        <>
            <ul className="nav">
                <li className="nav-item"><NavLink to='paises' className='nav-link'>Países</NavLink></li>
                <li className="nav-item"><NavLink to='provincias' className='nav-link'>Provincias</NavLink></li>
                <li className="nav-item"><NavLink to='localidades' className='nav-link'>Localidades</NavLink></li>
            </ul>

            <Outlet />
        </>
    )
}