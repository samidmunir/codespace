import styled from 'styled-components'

const StyledSidebar = styled.aside`
    background-color: var(--color-outer-space-100);
    padding: 10px 20px;
`

const Sidebar = () => {
    return (
        <StyledSidebar><h1>Sidebar</h1></StyledSidebar> 
    )
}

export default Sidebar