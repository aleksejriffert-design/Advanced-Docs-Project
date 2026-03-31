/**
 * @class UserService
 * @description Сервис управления пользователями LibraryAPI.
 */
class UserService {
    /**
     * Создает нового пользователя.
     * @param {string} email - Почта.
     * @param {Object} options - Настройки.
     * @param {string} [options.role='user'] - Роль (admin/user).
     * @returns {Promise<Object>} Данные пользователя.
     */
    async createUser(email, options = { role: 'user' }) {
        return { id: Date.now(), email, role: options.role };
    }

    /**
     * Удаляет пользователя.
     * @deprecated Используйте деактивацию вместо удаления.
     * @param {number} id - ID пользователя.
     */
    deleteUser(id) {
        console.log(`User ${id} deleted`);
    }
}
module.exports = UserService;