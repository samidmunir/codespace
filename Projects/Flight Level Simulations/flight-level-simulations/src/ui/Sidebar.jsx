import styled from 'styled-components'

import Logo from './Logo'

const StyledSidebar = styled.aside`
    background-color: var(--color-outer-space-100);
    padding: 10px 20px;
    border-right: 1px solid var(--color-cobalt-blue-100);
    grid-row: 1 / -1;
`

const Sidebar = () => {
    return (
        <StyledSidebar>
            <Logo />
        </StyledSidebar> 
    )
}

export default Sidebar