import React from 'react';
import { Link } from 'react-router-dom';
import { NavGroupItem } from 'client/src/ui/components/NavGroupItem';

const navGroups: NavGroupItem[] = [
    {
        code: 'leave',
        label: 'Leave Management',
        icon: 'fa fa-calendar',
        links: [
            { label: 'Leave Requests', to: '/leave-requests' },
            { label: 'Leave Types', to: '/leave-types' },
        ],
    },
    // other nav groups
];

const AppShellLayout: React.FC = ({ children }) => {
    return (
        <div>
            <nav>
                <ul>
                    {navGroups.map((group) => (
                        <li key={group.code}>
                            <h3>{group.label}</h3>
                            <ul>
                                {group.links.map((link) => (
                                    <li key={link.to}>
                                        <Link to={link.to}>
                                            {link.label}
                                        </Link>
                                    </li>
                                ))}
                            </ul>
                        </li>
                    ))}
                </ul>
            </nav>
            <main>{children}</main>
        </div>
    );
};

export default AppShellLayout;
