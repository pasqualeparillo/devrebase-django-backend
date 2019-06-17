import React, { useContext } from 'react'
import { Link } from "gatsby"
import {LoginContext} from '../../../../store/login'

export default function LoggedInWrapper() {
  const { setIsLoggedIn, isLoggedIn } = useContext(LoginContext)
    return (
        <>
        <button className="lg:px-6 lg:py-3 px-4 font-semibold text-blue-top text-xs "
          onClick={()=> {setIsLoggedIn(localStorage.removeItem('isLoggedIn'))}}>
            Logout
        </button>
           <button className="lg:px-6 lg:py-3 py-2 px-3 bg-green-light font-semibold  rounded shadow-md text-xs botton-hover-color hover:bg-green">
           <Link
            className="text-white no-underline"
            to="/profile">
             Profile
             </Link>
        </button>
        </>
    )
}