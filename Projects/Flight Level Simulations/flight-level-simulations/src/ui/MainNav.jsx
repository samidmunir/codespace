import { NavLink } from 'react-router-dom'
import styled from 'styled-components'

import {IoHome, IoBook, IoAlarm, IoAlertCircle, IoApps, IoInformationCircle, IoIdCard} from 'react-icons/io5'

const NavList = styled.ul`
    display: flex;
    flex-direction: column;
    gap: 12.5px;
`

const StyledNavLink = styled(NavLink)`
    &:link,
    &:visited {
        display: flex;
        align-items: center;
        gap: 19px;
        color: var(--color-grey-0);
        font-size: 20px;
        font-weight: 500;
        padding: 5px 10px;
        transition: all 0.3s ease-in-out;
    }

    &:hover,
    &:active,
    &.active:link,
    &.active:visited {
        color: var(--color-ucla-blue-100);
        background-color: var(--color-raisin-black-100);
        border-radius: 5px;
    }
`

const MainNav = () => {
    return (
        <nav>
            <NavList>
                <li>
                    <StyledNavLink to='/dashboard'>Home</StyledNavLink>
                </li>
                <li>
                    <StyledNavLink to='/blog'>Blog</StyledNavLink>
                </li>
                <li>
                    <StyledNavLink to='/schedules'>Schedules</StyledNavLink>
                </li>
                <li>
                    <StyledNavLink to='/featured'>Featured</StyledNavLink>
                </li>
                <li>
                    <StyledNavLink to='media'>Media</StyledNavLink>
                </li>
                <li>
                    <StyledNavLink to='/about'>About</StyledNavLink>
                </li>
                <li>
                    <StyledNavLink to='/contact'>Contact</StyledNavLink>
                </li>
            </NavList>
        </nav>
    )
}

export default MainNav