const { NUMBER } = require('sequelize');
const database = require('../models');

class PessoaController {

    // Read
    static async pegaTodasAsPessoas(req, res) {
        try {
            const todasAsPessoas = await database.Pessoas.findAll();
            return res.status(200).json(todasAsPessoas);
        } catch (err) {
            return res.status(500).json(err.message);
        }
    }

    // Read for ID
    static async pegaUmaPessoa(req, res) {
        const { id } = req.params
        try {
            const UmaPessoa = await database.Pessoas.findOne({
                where: {
                    id: Number(id)
                }
            });
            return res.status(200).json(UmaPessoa);
        } catch (err) {
            return res.status(500).json(err.message);
        }
    }

    // Create
    static async CadastrarPessoas(req, res) {
        const NovaPessoa = req.body
        try {
            if (Object.keys(NovaPessoa).length === 0) {
                throw new Error('corpo da requisição vazio');
            }
            const Registrar = await database.Pessoas.create(NovaPessoa);
            return res.status(201).json({ message: 'Pessoa criada', content: Registrar });
        } catch (err) {
            return res.status(500).json(err.message);
        }
    }

    // Update
    static async AtualizarPessoa(req, res) {
        const { id } = req.params;
        const MudarPessoa = req.body
        try {
            await database.Pessoas.update(MudarPessoa, { where: { id: Number(id) } });
            const Atualizar = await database.Pessoas.findOne({
                where: {
                    id: Number(id)
                }
            })
            return res.status(204).json({ message: 'Pessoa Atualizada', content: Atualizar });
        } catch (err) {
            return res.status(500).json(err.message);
        }
    }

    // Delete
    static async DeletarPessoa(req, res) {
        const { id } = req.params;
        try {
            await database.Pessoas.destroy({ where: { id: Number(id) } });
            return res.status(200).json({ message: 'Pessoa excluída' });
        } catch (err) {
            return res.status(500).json(err.message);
        }
    }

}

module.exports = PessoaController;
