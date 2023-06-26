import React from "react"
import { NavLink, Outlet } from "react-router-dom"

export default function Home() {
    return (
        <>
            <nav className="navbar navbar-expand-lg bg-light">
                <div className="container-fluid align-items-center p-4">
                    <NavLink to='/' className='navbar-brand'>Geolocación</NavLink>
                    <div className="collapse navbar-collapse">
                        <ul className="navbar-nav">
                            <li className="nav-item"><NavLink to='datos' className='nav-link'>Datos</NavLink></li>
                            <li className="nav-item"><NavLink to='consultas' className='nav-link'>Consultas</NavLink></li>
                        </ul>
                    </div>
                </div>
            </nav >
            <Outlet />
        </>
    )
}